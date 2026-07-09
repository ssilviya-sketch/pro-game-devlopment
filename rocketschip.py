import pygame,os,time
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("rocketship")
path1 = os.path.join("images","rocket.png")
path2 = os.path.join("images","space.png")
rocket = pygame.image.load(path1)
i1 = pygame.transform.scale(rocket,(40,40))
background = pygame.image.load(path2)
rocketx = 400
rockety = 400
keys = [False,False,False,False]
while rockety < 800:
    screen.blit(background,(0,0))
    screen.blit(i1,(rocketx,rockety))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_DOWN:
                keys[1] = True
            elif event.key == pygame.K_LEFT:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_DOWN:
                keys[1] = False
            elif event.key == pygame.K_LEFT:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False
    if keys[0]:
        if rockety > 0:
            rockety -= 10  
    if keys[1]:
        if rockety < 800:
            rockety += 10
    if keys[2]:
        if rocketx > 0:
            rocketx -= 10
    if keys[3]:
        if rocketx < 800:
            rocketx += 10
    rockety+=5
    time.sleep(1)
print("game over")
