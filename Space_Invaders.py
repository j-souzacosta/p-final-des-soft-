import pygame
import time
import random

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)

clock = pygame.time.Clock()
IDENTIFY_COLOR=pygame.Color(211,34,120)
pygame.init()
WIDTH=800
HEIGHT=600
#Tamanho da tela
#window = pygame.display.set_mode((800, 600))


all_sprites = pygame.sprite.Group()
tiros = pygame.sprite.Group()
inimigos = pygame.sprite.Group()

# class SpaceInvaders():
#     def __init__(self):
#         SCREEN_WIDTH = 1500
#         SCREEN_HEIGHT = 600
#         self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#         pygame.display.set_caption("Space Invaders")
        
        
        
#     def home_screen(self,playing): #Cria a tela inicial do jogo.
#         menu = True
#         Start = self.font.render(" ENTER : START ", True, WHITE, None)
#         Sair = self.font.render("   ESC : OUT      ", True, WHITE, None)
#         Start_rect = Start.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
#         Sair_rect = Sair.get_rect(center = ((SCREEN_WIDTH + 15) // 2, SCREEN_HEIGHT - 50))
#         self.window.fill(BLACK)
#         while menu:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     #music_menu.stop()
#                     return False
#                 if event.key == pygame.K_ESCAPE:
#                         music_menu.stop()
#                         return False
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
#                         playing = True()
#                         music_menu.stop()
#                         return True

#             self.window.fill(BLACK)
#             self.window.blit(Start, Start_rect)
#             self.window.blit(Sair, Sair_rect)
#             self.clock.tick(60)
#             pygame.display.update()

#         def main(self):
#             run = True
#             menu = True
        
#             while menu:
#                Start = self.home_screen()
            
#                if not Start:
#                     menu = False
#                     pygame.quit()
#                     exit()
        
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
        self.cooldown = 300

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
          
        
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.bottom < 0:
            self.kill()
    
class TiroAlien(pygame.sprite.Sprite): #Cria o tiro do alien
    def __init__(self,xy,direcao, GREEN, velocidade=8):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4,8))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = xy[0]
        self.rect.y = xy[1]
        self.direction = direcao
        self.speed = velocidade * direcao

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()    

class game:
    alienss = []

class Alien(pygame.sprite.Sprite): #cria imagem da nave e especifiões
    def __init__(self, img, x, y):# ,img_tiro_alien
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = img.get_rect()#para colisão definindo a imagem nave
        self.rect.x = x
        self.rect.y = y
        self.vx = 5
        self.vy = 0
        
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.atirar()
    
    def troca_de_lado(self):
        if self.rect.x > 1580 :
            #pygame.time.set_timer(self.descer,1000)
            self.vx = -5
            self.vy = 0
            
        elif self.rect.x < 50 :
            #pygame.time.set_timer(self.descer,1000) 
            self.vx = 5
            self.vy = 0

    def descer(self):
        self.vy = 1
        self.vx = 0

    def atirar(self): #Permite que os aliens atirem
        atirar = TiroAlien(self.rect.midtop, -1, GREEN, 4)
        all_sprites.add(atirar)
        return atirar

#def aliens(self, game):
    #margem = 25 #Espaço entre os aliens e a borda
    #espaco = 45 #Espaço entre os aliens
    #for x in range(margem, game.espaco - margem, espaco):
        #for y in range(margem, int(game.SCREEN_HEIGHT / 2), espaco):
            #game.alienss.append(Alien(game, x, y))




            
        

    
    


screen = pygame.display.set_mode((1720,802))#criador do display

pygame.display.set_caption('space invaders')
fundo=pygame.image.load('fundo11.gif')
nave_img = pygame.image.load("nave.png")
tiro_img=pygame.image.load('tiro4.png')
Alien_img=pygame.image.load("nave_marciano1.png")
#img_tiro_alien_img=pygame.image.load("tiro_alien.png")

# pygame.transform.rotate <- pesquisar
nave = Nave(nave_img, tiro_img)
margem = 25 #Espaço entre os aliens e a borda
espaco = 45 #Espaço entre os aliens
for x in range(margem, espaco - margem, espaco):
    for y in range(margem, int(game.SCREEN_HEIGHT / 2), espaco):
        alien = Alien(Alien_img, x, y)
        all_sprites.add(alien)
        
#nave_marciano_verde=pygame.image.load()
#nave_marciano_azul=pygame.image.load("nave_marciano_azul.png")

posicao_tiro_x=650
posicao_tiro_y=600

all_sprites.add(nave)
inimigos.add(alien)
playing=True
while playing:


    # move o quadrado um pixel por ciclo
    alien.troca_de_lado()
    #position_x +=0.01

    clock.tick(60)#deia o jogo em 60 fps

    screen.blit(fundo,(0,0)) # enche a tela de preto
    # posicao_tiro_x= position_x
    # posicao_tiro_y= position_y
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            playing=False
        
        if event.type==pygame.KEYDOWN:
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
                #nave.delay()
            if event.key == pygame.K_ESCAPE:
                playing=False
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_a:
                nave.vx += 10
            if event.key == pygame.K_d:
                nave.vx -= 10
            if event.key == pygame.K_w:
                nave.vy += 10
            if event.key == pygame.K_s:
                nave.vy -= 10
            
                
    

    # desenha o quadrado em sua nova posição



    #pygame.draw.rect(screen, IDENTIFY_COLOR, [position_x, position_y, 50, 50])
    
    all_sprites.update()
    all_sprites.draw(screen)

    #screen.blit(nave_marciano_azul,(posição_nave1_x,posicao_nave1_y))
    #screen.blit(nave_marciano_azul,(650,300))

    #screen.blit(nave_marciano_verde,(650,100))


    #pygame.draw.rect(screen, IDENTIFY_COLOR, [posicao_tiro_x, posicao_tiro_y, 10, 10])

    pygame.display.flip()
    
