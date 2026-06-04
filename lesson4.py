import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("robothead")
running = True
while running:
    screen.fill((30,40,255))
    pygame.draw.rect(screen,(255,255,255),(300,300,350,350),6)
    pygame.draw.circle(screen,(255,255,255),(375,375),20,6)
    pygame.draw.circle(screen,(255,255,255),(550,375),20,6)



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
pygame.quit()


