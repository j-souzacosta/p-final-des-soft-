#importa as bibliotecas necessarias
import pygame
import time
import random
from pygame import mixer 

# definições de algumas cores 

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)

# arquivo de audio utilizado no no jogo 
file = 'music_menu.mp3'

#inicialização do jogo e do mixer 
clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
WIDTH=800
HEIGHT=600
#Tamanho da tela

x=100
y=100

all_sprites = pygame.sprite.Group()
tiros = pygame.sprite.Group()
player = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
tiros_inimigos = pygame.sprite.Group()
   

#Faz load e toca a musica
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait(-1)
pygame.mixer.music.set_volume(0.25)

def home_screen(screen): #Cria a tela inicial do jogo.
    playing = True
    screen.blit(Menu_img,(0,0)) #Coloca a imagen de menu na tela
    while playing:
        for event in pygame.event.get(): #Faz com que seja posivel fechar o jogo   
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Fecha o jogo apertando "ESC"
                    return False
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE: # Começa o jogo apertando a barra de espaço ou enter
                    return True

        pygame.display.update() # da um uptade na tela

class SpaceInvaders():
    def __init__(self):
        SCREEN_WIDTH = 1500
        SCREEN_HEIGHT = 600
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Invaders")
        
class Nave(pygame.sprite.Sprite): #cria imagem da nave e especifiões
    def __init__(self, img, img_tiro,):#
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = img.get_rect()#para colisão definindo a imagem nave
        self.rect.x = 650
        self.rect.y = 550
        self.vx = 0
        self.vy = 0
        self.img_tiro = img_tiro
        self.last = pygame.time.get_ticks()
        self.cooldown = 500

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
    
    def atira(self):# para repitir o tiro
        now = pygame.time.get_ticks()
        
        if now - self.last >= self.cooldown:
            self.last = now   
            tiro = Tiro(self.img_tiro, self.rect.centerx, self.rect.y)
            all_sprites.add(tiro)
            tiros.add(tiro)



class Tiro(pygame.sprite.Sprite):
    def __init__(self, img, cx, by):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = img.get_rect()#para colisão definindo a imagem nave
        self.rect.centerx = cx
        self.rect.bottom = by
        self.vx = 0
        self.vy = -4
          
        
    
    def update(self): # movimentação do tiro do aliado 
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.bottom < 0:
            self.kill()
    
class TiroAlien(pygame.sprite.Sprite): #Cria o tiro do alien
    def __init__(self,xy,direcao, GREEN, velocidade=8):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,16)) # tamanho do tiro do alien 
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = xy[0]
        self.rect.y = xy[1]
        self.direction = direcao
        self.speed = velocidade * direcao

    def update(self):# velocidade do tiro do alien 
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()    

#class game:
#    alienss = []

class Alien(pygame.sprite.Sprite): #cria imagem da nave e especifiões
    def __init__(self, img, x, y):# ,img_tiro_alien
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = img.get_rect()#para colisão definindo a imagem nave
        self.rect.x = x
        self.rect.y = y
        self.vx = 5
        self.vy = 0
        self.last = pygame.time.get_ticks()
        p = random.randint(1000,10000) # taxa de tiros das naves inimigas 
        self.cooldown = p
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.atirar()
        self.troca_de_lado()
        
    # especificando movimentação da nave     
    
    def troca_de_lado(self):
        if self.rect.x > 1580 :
            self.vx = -5
            self.vy = 0
            
            
        elif self.rect.x < 50 :
            
            self.vx = 5
            self.vy = 0

    def descer(self):
            self.vy = 1
            self.vx = 0


    def atirar(self): #Permite que os aliens atirem
        now = pygame.time.get_ticks()

        if now - self.last >= self.cooldown:
            self.last = now
            atirar = TiroAlien(self.rect.midtop, -1, GREEN, 6)
            all_sprites.add(atirar)
            tiros_inimigos.add(atirar)
        #return atirar
        #tiro = Tiro(self.img_tiro, self.rect.centerx, self.rect.y)
        #    all_sprites.add(tiro)
        #    tiros.add(tiro)

def game_screen(screen):
    x=100
    y=100
    m = 0
    vidas = 3
    j=0
    nave = Nave(nave_img, tiro_img)
    alien = Alien(Alien_img,x,y)
    b=0
    #Criar vários aliens
    margem = 25 #Espaço entre os aliens e a borda
    espaco = 100 #Espaço entre os aliens
    for x in range(margem, 1600, espaco):
        for y in range(margem, int(802 / 3), espaco):
            alien = Alien(Alien_img, x, y)
            all_sprites.add(alien)
            inimigos.add(alien)
            b +=1 # numero de aliens totais
            
    
           
            
    #nave_marciano_verde=pygame.image.load()
    #nave_marciano_azul=pygame.image.load("nave_marciano_azul.png")

    posicao_tiro_x=650
    posicao_tiro_y=600

    all_sprites.add(nave)
    player.add(nave)

    playing=True

    

    while playing:


        # move o quadrado um pixel por ciclo

        clock.tick(60)#deia o jogo em 60 fps

        screen.blit(fundo,(0,0)) # enche a tela de preto

        all_sprites.add(nave)
        player.add(nave)
        events = pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT: # linha para sair do jogo 
                return False
            
            if event.type==pygame.KEYDOWN: # designação de teclas para a movimentação e tiro  w, a ,s, d, space
                if event.key == pygame.K_a:
                    nave.vx -= 10
                if event.key == pygame.K_d:
                    nave.vx += 10
                if event.key == pygame.K_w:
                    nave.vy -= 10
                if event.key == pygame.K_s:
                    nave.vy += 10
                if event.key == pygame.K_SPACE:
                    nave.atira()
                if event.key == pygame.K_ESCAPE:
                    playing = home_screen(screen)
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_a:
                    nave.vx += 10
                if event.key == pygame.K_d:
                    nave.vx -= 10
                if event.key == pygame.K_w:
                    nave.vy += 10
                if event.key == pygame.K_s:
                    nave.vy -= 10
                
  
        #colisão dos objetos 

        # desenha o quadrado em sua nova posição

        #Cria colisao
        hits = pygame.sprite.spritecollide(nave, inimigos, True)
        hits_I = pygame.sprite.groupcollide(inimigos, tiros, True,True)
        hits_TI = pygame.sprite.spritecollide(nave,tiros_inimigos, True)

        #Perde uma vida se o tiro acertar a nave
        if hits or hits_TI: #checa colisão entre o tiro aliado com as naves inimigas 
            vidas = vidas -1 # tira 1 de suas vidas es for atingido
            if vidas == 0:
                screen.blit(gameover_img,(0,0)) # Mostra a tela de derrota
                pygame.display.flip()
                pygame.time.wait(2500) # Espera um pouco antes
                playing = home_screen(screen) # Volta para tela inicial

                #Reseta o jogo
                x=100
                y=100
                m = 0
                vidas = 3
                j=0
                b=0
                nave.vy = 0
                nave.vx = 0
                nave.rect.x = 650
                nave.rect.y = 550
                margem = 25 
                espaco = 100 
                all_sprites.remove(inimigos)
                inimigos.empty()
                all_sprites.remove(player)
                player.empty()
                all_sprites.remove(tiros_inimigos)
                tiros_inimigos.empty()
                all_sprites.remove(tiros)
                tiros.empty()
                for x in range(margem, 1600, espaco):
                    for y in range(margem, int(802 / 3), espaco):
                        alien = Alien(Alien_img, x, y)
                        all_sprites.add(alien)
                        inimigos.add(alien)
                        b +=1
                    
        for hit in hits_I or hits: # checa colisão entre o tiro do inimigo e a nave aliada 
            #tira 1 do numero total de aliens,, ja que acertou um
            b = b-1
            if b == 0: #Checa se matou todos os aliens

                screen.blit(ganhou_img,(0,0)) # Mostra a tela de vitoria
                pygame.display.flip()
                pygame.time.wait(2500) # espera um pouco antes de fazer o proximo passo
                playing = home_screen(screen) # Abre a tela inicial novamente
                
                #Reseta o jogo
                x=100
                y=100
                m = 0
                vidas = 3
                j=0
                b=0
                nave.vy = 0
                nave.vx = 0
                nave.rect.x = 650
                nave.rect.y = 550
                #Criar vários aliens
                margem = 25 #Espaço entre os aliens e a borda
                espaco = 100 #Espaço entre os aliens
                all_sprites.remove(inimigos)
                inimigos.empty()
                all_sprites.remove(player)
                player.empty()
                all_sprites.remove(tiros_inimigos)
                tiros_inimigos.empty()
                all_sprites.remove(tiros)
                tiros.empty()
                for x in range(margem, 1600, espaco):
                    for y in range(margem, int(802 / 3), espaco):
                        alien = Alien(Alien_img, x, y)
                        all_sprites.add(alien)
                        inimigos.add(alien)
                        b +=1
                        
        all_sprites.update()
        all_sprites.draw(screen)
        
        if vidas != 0:# imprime na tela a vida do jogador 
            for j in range(vidas):        
                screen.blit(vida_img,(100 * j ,700))
                pygame.display.flip()
                

        pygame.display.flip()
        
screen = pygame.display.set_mode((1720,802))#criador do display


#Carega as imagens 
pygame.display.set_caption('Space Invaders')
fundo=pygame.image.load('fundo11.gif')
gameover_img=pygame.image.load('gameover.png')
nave_img = pygame.image.load("nave.png")
tiro_img=pygame.image.load('tiro4.png')
Alien_img=pygame.image.load("nave_marciano1.png")
Menu_img=pygame.image.load("tela inicial.png")
vida_img=pygame.image.load("vidaa.png")
ganhou_img=pygame.image.load("YOU WIN.png")

 
playing = True
# Roda o jogo ou a tela de inicio
while playing:
    playing = home_screen(screen)
    if playing:
        playing = game_screen(screen)
    else:
        pygame.quit()
        
        