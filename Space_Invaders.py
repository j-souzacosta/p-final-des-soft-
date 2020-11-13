import pygame
import time

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
IDENTIFY_COLOR=pygame.Color(211,34,120)
pygame.init()


all_sprites = pygame.sprite.Group()
tiros = pygame.sprite.Group()


class Nave(pygame.sprite.Sprite): #cria imagem da nave e especifiões
    def __init__(self, img, img_tiro):#
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = img.get_rect()#para colisão definindo a imagem nave
        self.rect.x = 650
        self.rect.y = 550
        self.vx = 0
        self.vy = 0
        self.img_tiro = img_tiro
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
    
    def atira(self):# para repitir o tiro
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

class Alien(pygame.sprite.Sprite): #cria imagem da nave e especifiões
    def __init__(self, img):#
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = img.get_rect()#para colisão definindo a imagem nave
        self.rect.x = 100
        self.rect.y = 100
        self.vx = 1
        self.vy = 0
        
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        



screen = pygame.display.set_mode()#criador do display

pygame.display.set_caption('space invaders')

nave_img = pygame.image.load("nave.png")
tiro_img=pygame.image.load('tiro.png')
Alien_img=pygame.image.load("nave_marciano1.png")
# pygame.transform.rotate <- pesquisar
nave = Nave(nave_img, tiro_img)
alien = Alien(Alien_img)
#nave_marciano_verde=pygame.image.load()
#nave_marciano_azul=pygame.image.load("nave_marciano_azul.png")

posicao_tiro_x=650
posicao_tiro_y=600

all_sprites.add(nave)
all_sprites.add(alien)
playing=True

while playing:


    # move o quadrado um pixel por ciclo

    #position_x +=0.01


    screen.fill(BLACK) # enche a tela de preto
    # posicao_tiro_x= position_x
    # posicao_tiro_y= position_y
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_a:
                nave.vx -= 1
            if event.key == pygame.K_d:
                nave.vx += 1
            if event.key == pygame.K_w:
                nave.vy -= 1
            if event.key == pygame.K_s:
                nave.vy += 1
            if event.key == pygame.K_SPACE:
                nave.atira()
            if event.key == pygame.K_ESCAPE:
                playing=False
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_a:
                nave.vx += 1
            if event.key == pygame.K_d:
                nave.vx -= 1
            if event.key == pygame.K_w:
                nave.vy += 1
            if event.key == pygame.K_s:
                nave.vy -= 1
            
                
    

    # desenha o quadrado em sua nova posição



    #pygame.draw.rect(screen, IDENTIFY_COLOR, [position_x, position_y, 50, 50])
    
    all_sprites.update()
    all_sprites.draw(screen)

    #screen.blit(nave_marciano_azul,(posição_nave1_x,posicao_nave1_y))
    #screen.blit(nave_marciano_azul,(650,300))

    #screen.blit(nave_marciano_verde,(650,100))

    








    #pygame.draw.rect(screen, IDENTIFY_COLOR, [posicao_tiro_x, posicao_tiro_y, 10, 10])

    pygame.display.flip()
