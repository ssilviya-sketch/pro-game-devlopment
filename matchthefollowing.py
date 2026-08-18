import pygame,os
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("matchthefollowing")
screen.fill((255,255,255))
path1 = os.path.join("images","subwaysurfer.png")
path2 = os.path.join("images","ludo.png")
path3 = os.path.join("images","templerun(1).png")
path4 = os.path.join("images","candycrush.jpg")
image1 = pygame.image.load(path1)
image2 = pygame.image.load(path2)
image3 = pygame.image.load(path3)
image4 = pygame.image.load(path4)
font = pygame.font.SysFont("Arial",36)
running = True
screen.blit(image1,(200,375))
screen.blit(image2,(200,275))
screen.blit(image3,(200,175))
screen.blit(image4,(200,75))
t1 = font.render("templerun",True,(0,0,0))
t2 = font.render("ludo",True,(0,0,0))
t3 = font.render("candycrush",True,(0,0,0))
t4 = font.render("subwaysurfer",True,(0,0,0))
screen.blit(t1,(400,375))
screen.blit(t2,(400,275))
screen.blit(t3,(400,175))
screen.blit(t4,(400,75))
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()