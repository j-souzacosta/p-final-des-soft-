import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
IDENTIFY_COLOR=pygame.Color(211,34,120)
pygame.init()


screen = pygame.display.set_mode()#criador do display

pygame.display.set_caption('space invaders')

nave = pygame.image.load("nave.png")
nave_marciano_verde=pygame.image.load("nave_marciano1.png")
#nave_marciano_azul=pygame.image.load("nave_marciano_azul.png")

posição_nave1_x=650
posicao_nave1_y=100



posicao_tiro_x=600
posicao_tiro_y=600


position_x=650
position_y=550

playing=True

while playing:
    

    # move o quadrado um pixel por ciclo
    
    #position_x +=0.01
    
    
    screen.fill(BLACK) # enche a tela de preto

    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            playing=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        position_x -=0.5
    if keys[pygame.K_d]:
        position_x +=0.5
    if keys[pygame.K_w]:
        position_y -=0.5
    if keys[pygame.K_s]:
        position_y +=0.5
   
    posicao_tiro_y -=0.5
   
    # desenha o quadrado em sua nova posição
    

    
    #pygame.draw.rect(screen, IDENTIFY_COLOR, [position_x, position_y, 50, 50])
    screen.blit(nave,(position_x,position_y,))

    #screen.blit(nave_marciano_azul,(posição_nave1_x,posicao_nave1_y))
    #screen.blit(nave_marciano_azul,(650,300))
    
    screen.blit(nave_marciano_verde,(650,100))

    #pygame.draw.rect(screen, IDENTIFY_COLOR, [posicao_tiro_x, posicao_tiro_y, 10, 10])

    pygame.display.flip()
