import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("draw colours")
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
screen.fill(white)
class s:
    def __init__(self,screen,color):
        self.screen = screen
        self.color = color
    def draw_rect(self):
        pygame.draw.rect(self.screen,self.color,(400,400,300,200))
r = s(screen,red)
g = s(screen,green)
b = s(screen,blue)
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.draw.rect(screen,red,(400,400,300,200))
                r.draw_rect()
            elif event.key == pygame.K_2:
                pygame.draw.rect(screen,green,(400,400,300,200))
                g.draw_rect()
            elif event.key == pygame.K_3:
                pygame.draw.rect(screen,blue,(400,400,300,200))
                b.draw_rect()
    pygame.display.update()
pygame.quit()