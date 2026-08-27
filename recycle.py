import pygame,os,random,time
pygame.init()
screen = pygame.display.get_mode((800,800))
pygame.display.set_caption("recycle game")
path1 = os.path.join("images","item1.jpg")
path2 = os.path.join("images","item2.jpg")
path3 = os.path.join("images","item3.jpg")
path4 = os.path.join("images","no.jpg")
path5 = os.path.join("images","bin.jpg")
path6 = os.path.join("images","bg.jpg")
i1 = pygame.image.load(path1)
i2 = pygame.image.load(path2)
i3 = pygame.image.load(path3)
i4 = pygame.image.load(path4)
i5 = pygame.image.load(path5)
bg = pygame.image.load(path6)
bin = pygame.transform.scale(i5,(40,60))
plasticbag = pygame.transform.scale(i4,(40,40))
r1 = pygame.transform.scale(i1,(30,30))
r2 = pygame.transform.scale(i2,(30,30))
r3 = pygame.transform.scale(i3,(30,30))
recycableimages = [r1,r2,r3]
binrect = bin.get_rect(center = (450,350))
items = []
for _ in range(50):
    img = random.choice(recycableimages)
    rect = img.get_rect(x = random.randrange(790),y = random.randrange(790))
    items.append((img,rect))
plasticlist = []
for _ in range(25):
    plasticrect = plasticbag.get_rect(x = random.randrange(790),y = random.randrange(790))
    plasticlist.append(plasticrect)
red = (255,0,0)
blue = (0,0,255)
font = pygame.font.sysfont("Ariel",36)
score = 0
starttime = time.time()
running = True
def changeimg(gameend):
    p = os.path.join("images",gameend)
    b = pygame.image.load(p)
    bg = pygame.transform.scale(800,800)
    screen.blit(bg,(0,0))
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    elapsetime = time.time()-starttime
    if elapsetime >= 60:#if elapse time is greater then 60 we want to end the game
        if score > 100:
            w = font.render("you won the game",True,(0,0,0))
            changeimg("youwin.jpg")
        else:
            l = font.render("you lost the game",True,(0,0,0))
            changeimg("youlose.jpg")
    else:
        changeimg("bg.jpg")
        timer = font.render("Time left:"+str(60-int(elapsetime)),True,(0,0,0))
        