import pygame
import random

W,H=500,500
object_to_draw=''
pygame.init()
win=pygame.display.set_mode((W,H))

win.fill((255, 255, 255))
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    pos=pygame.mouse.get_pos()
    x=pos[0]
    y=pos[1]
    keys=pygame.key.get_pressed()
    if keys[pygame.K_q]:
       object_to_draw= 'квадрат'
    if keys[pygame.K_w]:
       object_to_draw='круг'
    if object_to_draw=='круг':
        pygame.draw.circle(win, random.choices(range(256), k=3), (x, y), 30)
    if object_to_draw == 'квадрат':
        pygame.draw.rect(win, random.choices(range(256), k=3), (x, y, 50, 50))
    pygame.display.update()
    pygame.time.delay(10)