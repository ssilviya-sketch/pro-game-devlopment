import pygame,os
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("space invaders")
r = (255,0,0)
white = (255,255,255)
black = (0,0,0)
y = (255,255,0)
fps = 60
vel = 5#velocity means how fast something goes and this is for the velocity for the spaceships
bulvel = 7# this is the velocity for the bullets
max_bull = 3
space_ship_width = 55
space_ship_height = 40
path1 = os.path.join("images","spaceship_red.png")
path2 = os.path.join("images","spaceship_yellow.png")
path3 = os.path.join("images","copy of space.png")
image1 = pygame.image.load(path1)
i1 = pygame.transform.scale(space_ship_height,space_ship_width)
image2 = pygame.image.load(path2)
i2 = pygame.transform.scale(space_ship_height,space_ship_width)
image3 = pygame.image.load(path3)
i3 = pygame.transform.scale(800,800)
yellow_spaceship = pygame.transform.rotate(i1,90)
red_spaceship = pygame.transform.rotate(i2,270)
border = pygame.Rect(395,0,10,800)
def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(i3,(0,0))
    pygame.draw.rect(border,(0,0,0))

