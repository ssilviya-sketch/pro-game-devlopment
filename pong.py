import pygame,os,time
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("pong")
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
fps = 60
vel = 5
bulvel = 7
max_bull = 3
keypress = pygame.key.get_pressed()
pong1hit = pygame.USEREVENT+1
pong2hit = pygame.USEREVENT+2
pongwidth = 55
pongheight = 40
path1 = os.path.join("images","pong1.png")
path2 = os.path.join("images","pong2.png")
path3 = os.path.join("images","copy_of_space.png")
path4 = os.path.join("images","pongball.jpg")
image1 = pygame.image.load(path1)
i1 = pygame.transform.scale(image1,(pongwidth,pongheight))
image2 = pygame.image.load(path2)
i2 = pygame.transform.scale(image2,(pongwidth,pongheight))
image4 = pygame.image.load(path4)
ball = pygame.transform.scale(image4,(40,40))
image3 = pygame.image.load(path3)
i3 = pygame.transform.scale(image3,(800,800))
pong1 = pygame.transform.rotate(i1,90)
pong2 = pygame.transform.rotate(i2,270)
border = pygame.Rect(395,0,10,800)
running = True
while running:
    screen.blit(i3,(0,0))
    screen.blit(pong1,(100,400))
    screen.blit(pong2,(700,400))
    pygame.draw.rect(screen,(0,0,0),border)
    pygame.display.update()
def pong1_movement(keypress,pong1):
    if keypress[pygame.K_w]and pong1.y-vel > 0:
        pong1.y-=vel
    if keypress[pygame.K_s]and pong1.y+vel+pong1.height < 785:
        pong1.y+=vel
def pong2_movement(keypress,pong2):
    if keypress[pygame.K_UP]and pong2.y-vel > 0:
        pong2.y-=vel
    if keypress[pygame.K_DOWN]and pong2.y+vel+pong2.height < 785:
        pong2.y+=vel
def ball_movement():
    while 1:
        ball.x+=20
        if pong1.colliderect(ball):
            ball.x+=20
        if pong2.colliderect(ball):
            ball.x-=20
        if ball.x < 0 or > 800:
            break
pong1 = pygame.Rect(700,400)
pong2 = pygame.Rect(100,400)
ball = pygame.Rect(400,400)
def main():
    clock = pygame.time.Clock()
    while 1:
        pong1_movement()
        pong2_movement()





