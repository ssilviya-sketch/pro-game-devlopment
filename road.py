import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("car road")
running = True
while running:
    pygame.draw.rect(screen,(255,255,255),(375,500,300,200),5)
    pygame.draw.rect(screen,(43,255,31),(380,550,20,10),5)
    pygame.draw.rect(screen,(255,100,31),(410,550,20,10),5)
    pygame.draw.rect(screen,(31,255,255),(440,550,20,10),5)





    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
pygame.quit()
