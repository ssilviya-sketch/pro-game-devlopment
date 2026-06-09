import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("mouseclick")
blue = (0,0,255)
screen.fill(blue)
red = (255,0,0)
class circle:
    def __init__(self,color,position,radius,width):
        self.color = color
        self.position = position
        self.radius = radius
        self.width = width
        self.surface = screen
    def draw(self):
        self.drawcircle = pygame.draw.circle(self.surface,self.color,self.position,self.radius,self.width)
c1 = circle(red,(400,400),30,0)
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(blue)
            c1.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill(blue)
            pygame.display.update()
pygame.quit()
    