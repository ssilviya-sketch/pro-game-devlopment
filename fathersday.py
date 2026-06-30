import pygame,time,os
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("fatherdaycard")
path1 = os.path.join("images","beach.jpg")
path2 = os.path.join("images","flower.jpg")
path3 = os.path.join("images","presents.png")
image1 = pygame.image.load(path1)
i1 = pygame.transform.scale(image1,(800,800))
image2 = pygame.image.load(path2)
i2 = pygame.transform.scale(image2,(800,800))
image3 = pygame.image.load(path3)
i3 = pygame.transform.scale(image3,(800,800))
font1 = pygame.font.SysFont("Times New Roman",72)
font2 = pygame.font.SysFont("Arial",36)
running = True
while running:
    screen.blit(i1,(0,0))
    t1 = font1.render("Happy fathersday",True,(0,0,0))
    screen.blit(t1,(300,400))
    pygame.display.update()
    time.sleep(3)
    screen.fill((255,255,255))
    screen.blit(i2,(0,0))
    t3 = font2.render("I hope you will have a relaxing day",True,(0,0,0))
    screen.blit(t3,(200,200))
    pygame.display.update()
    time.sleep(3)
    screen.blit(i3,(0,0))
    t4 = font2.render("I love you dad",True,(0,0,0))
    screen.blit(t4,(300,300))
    pygame.display.update()
    time.sleep(3)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
    