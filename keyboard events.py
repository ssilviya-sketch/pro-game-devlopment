import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("draw shapes")
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
screen.fill(white)
class shapes:
    def __init__(self,screen):
        self.screen = screen
    def draw_rect(self):
        pygame.draw.rect(self.screen,black,(400,400,300,200))
    def draw_circ(self):
        pygame.draw.circle(self.screen,red,(200,200),30)
    def draw_line(self):
        pygame.draw.line(self.screen,green,(500,550),(748,748),4)
canvas = shapes(screen)
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                canvas.draw_rect()
            elif event.key == pygame.K_s:
                canvas.draw_circ()
            elif event.key == pygame.K_l:
                canvas.draw_line()
    pygame.display.update()
pygame.quit()
