import pygame

pygame.init()

width = 500
height = 500
cx = width/2
cy = height/2
x = 1
y = 1

win = pygame.display.set_mode((width,height))
xCircle = width/2
yCircle = height/2

colour = (255,255,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        xCircle -= 5
    elif keys[pygame.K_d]:
        xCircle += 5
    elif keys[pygame.K_w]:
        yCircle -= 5
    elif keys[pygame.K_s]:
        yCircle += 5
    else:
        xCircle = width/2
        yCircle = height / 2

    if xCircle > cx + 100:
        colour = (255, 0, 0)
    elif xCircle < cx - 100:
        colour = (255, 0, 0)
    elif yCircle > cy + 100:
        colour = (255, 0, 0)
    elif yCircle < cy - 100:
        colour = (255, 0, 0)
    else:
        colour = (255, 255, 0)

    win.fill((255,255,255))

    pygame.draw.circle(win,colour,(xCircle,yCircle),30)
    pygame.display.update()
    pygame.time.delay(10)