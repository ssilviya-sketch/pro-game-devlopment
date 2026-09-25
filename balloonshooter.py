import pygame,os,random
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("balloonshooter")
p1 = os.path.join("images","balloon.jpg")
p2 = os.path.join("images","rock.png")
p3 = os.path.join("images","gun.jpg")
i1 = pygame.image.load(p1)
i2 = pygame.image.load(p2)
i3 = pygame.image.load(p3)
balloon = pygame.transform.scale(i1,(60,60))
rock = pygame.transform.scale(i2,(60,60))
gun = pygame.transform.scale(i3,(60,60))
gun = pygame.transform.rotate(gun,90)
gun_rect = gun.get_rect()
gun_rect.x = 370
gun_rect.y = 700
vel = 1
bulvel = 2
balloons = []
bullets = []
max_bull = 2000
score = 0
rocks = []
balloonhit = pygame.USEREVENT+1
rockhit = pygame.USEREVENT+2
def draw_window(score):
    screen.fill((255,255,255))
    font = pygame.font.SysFont("Times New Roman",30)
    score = font.render("score:"+str(score),True,(0,0,0))
    screen.blit(score,(200,750))
    screen.blit(gun, gun_rect)
    for balloon_rect in balloons: 
        screen.blit(balloon,balloon_rect) 
    for rock_rect in rocks: 
        screen.blit(rock,rock_rect)
def gun_movement(keypress):
    if keypress[pygame.K_a]:
       gun_rect.x-=vel
    if keypress[pygame.K_d]:
        gun_rect.x+=vel
def fall():
    for balloon_rect in balloons:
        balloon_rect.y += 0.5
    for rock_rect in rocks:
        rock_rect.y += 0.5
def spawn_balloon():
    rect = balloon.get_rect(x=random.randrange(740),y=-60)
    balloons.append(rect)
def spawn_rock():
    rect = rock.get_rect(x=random.randrange(740),y=-60)
    rocks.append(rect)
def Handling_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen,(255,30,0),bullet)
        bullet.y-=bulvel
        for balloon_rect in balloons[:]:
            if balloon_rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(balloonhit))
                balloons.remove(balloon_rect)
        for rock_rect in rocks[:]:
            if rock_rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(rockhit))
                rocks.remove(rock_rect)
balloon_timer = 0
rock_timer = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and len(bullets) < max_bull:
                bullet = pygame.Rect(gun_rect.x+gun_rect.width,gun_rect.y+gun_rect.height//2-2,10,5)
                bullets.append(bullet)
        if event.type == balloonhit:
            score+=2
        if event.type == rockhit:
            score-=3
    keypress = pygame.key.get_pressed()
    fall()
    gun_movement(keypress)
    draw_window(score)
    Handling_bullets()
    balloon_timer += 1
    rock_timer += 1
    if balloon_timer >= 60:
      spawn_balloon()
      balloon_timer = 0
    if rock_timer >= 120:
      spawn_rock()
      rock_timer = 0
    pygame.display.update()
pygame.quit()