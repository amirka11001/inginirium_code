import random

import pygame

pygame.init()
size=W,H=700,700
FPS=30
win=pygame.display.set_mode(size)

img=pygame.image.load('inzh.png')

class Inginirium(pygame.sprite.Sprite):
    def __init__(self,*group):
        super().__init__(*group)
        self.image=load_image('inzh.png')
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(W)
        self.rect.x = random.randrange(H)

    def update(self):
        self.rect=self.rect.move(random.randrange(3)-1,
                                 random.randrange(3)-1)
def load_image(name):
    img=pygame.image.load(name)
    img=img.convert()
    colorkey=img.get_at((0,0))
    img.set_colorkey(colorkey)
    return img

all_sprites=pygame.sprite.Group()
for i in range(50):
    Inginirium(all_sprites)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()

    win.fill((255,255,255))
    all_sprites.draw(win)
    all_sprites.update()
    pygame.display.update()