import pygame,os
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("floating rocket")
path1 = os.path.join("images","rocket.png")
path2 = os.path.join("images","space.png")
rocket = pygame.image.load(path1)
i1 = pygame.transform.scale(rocket,(40,40))
background = pygame.image.load(path2)
rocketx = 400
rockety = 400
running = True
while running:
    screen.blit(background,(0,0))
    screen.blit(i1,(rocketx,rockety))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                 rockety -= 10
pygame.quit()