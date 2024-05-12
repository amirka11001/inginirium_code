import random

import pygame

# Инициализация Pygame
pygame.init()


class Player(pygame.sprite.Sprite):
    # Создаем конструктор
    def __init__(self, *group):
        # Вызываем конструктор у родительского класса(Sprite)
        super().__init__(*group)
        # Загружаем изображение игрока
        self.image = pygame.image.load('капхед.png')
        # Настраиваем размер изображения
        self.image = pygame.transform.scale(self.image, (110, 150))
        self.is_jump=False
        self.jump_counter=30
        self.rect = self.image.get_rect()
        self.rect.y=400
        self.health=3
        self.to_left = False
        self.to_right = True

    # Создаем функцию обновления спрайта
    def update(self):
        # Вызываем функцию движения
        self.move_by_keys()

    # Создаем функцию движения
    def move_by_keys(self):
        keys = pygame.key.get_pressed() # Получаем все нажатые клавиши
        if keys[pygame.K_a]: # Если нажата клавиша A
            self.image = pygame.image.load('капхед2.png')
            self.image = pygame.transform.scale(self.image, (110, 150))
            self.rect.left -= 10 # Двигаемся влево на 5 пикселей
            self.to_left = True
            self.to_right = False
        if keys[pygame.K_d]: # Если нажата клавиша D

            self.image = pygame.image.load('капхед.png')
            self.image = pygame.transform.scale(self.image, (110, 150))
            self.rect.left += 7
            self.to_right = True
            self.to_left = False
        if keys[pygame.K_SPACE]:
            self.is_jump=True
        if self.is_jump:
            if self.jump_counter>=-30:
                self.rect.top-=self.jump_counter
                self.jump_counter-=2
            else:
                self.jump_counter=30
                self.is_jump=False
        #if keys[pygame.K_f]:
        #    bullet = Bullet()
        #    bullet_sprites.add(bullet)


class Enemy(pygame.sprite.Sprite):
    # Создаем инициализатор(конструктор)
    def __init__(self):
        # Вызываем конструктор самого класса Sprite
        super().__init__()
        # Загружаем изображение
        self.image = pygame.image.load('враг.png')
        # Настраиваем его. Не нужно здесь ничего менять, просто копируйте
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        # Задаем размер. Первая 100 - ширина, вторая 100 - высота
        self.image = pygame.transform.scale(self.image, (100, 100))
        # Задаем границы
        self.rect = self.image.get_rect()
        self.dir = 'right'
        self.health = 5
    def update(self):
        if self.rect.right>width:
            self.image = pygame.image.load('враг.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.dir = 'left'
            self.rect.x = 900
        if self.rect.left<0:
            self.dir = 'right'
            self.image = pygame.image.load('враг2.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            #self.rect.left+=5
        if self.dir == 'right':
            self.rect.left += 6
        elif self.dir == 'left':
            self.rect.left -= 6
        self.rect.y = 470

class Bullet(pygame.sprite.Sprite):
    # Создаем конструктор
    def __init__(self, *group):
        # Вызываем конструктор у родительского класса(Sprite)
        super().__init__(*group)
        # Загружаем изображение игрока
        self.image = pygame.image.load('пуля.png')
        # Настраиваем размер изображения
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centery=player.rect.centery
        self.rect.left=player.rect.right
        self.to_left = False
        self.to_right = True
    def update(self):
        if self.to_right:
            self.rect.right+=5
        elif self.to_left:
            self.rect.left -= 5




class Bird(pygame.sprite.Sprite):
    # Создаем инициализатор(конструктор)
    def __init__(self):
        # Вызываем конструктор самого класса Sprite
        super().__init__()
        # Загружаем изображение
        self.image = pygame.image.load('Птица.png')
        # Задаем размер. Первая 100 - ширина, вторая 100 - высота
        self.image = pygame.transform.scale(self.image, (50, 50))
        # Задаем границы
        self.rect = self.image.get_rect()
        self.rect.y = 100
        self.dir = 'right'
        self.health = 5

    def update(self):
        if self.rect.right>width:
            #self.rect.left-=5
            self.dir = 'left'
        if self.rect.left<0:
            self.dir = 'right'
            #self.rect.left+=5
        if self.dir == 'right':
            self.rect.left += 1
        elif self.dir == 'left':
            self.rect.left -= 1
pygame.init()

# Создаем переменные ширины и высоты экрана
width = 1000
height = 600

# Создаем окно с заранее созданными размерами
win = pygame.display.set_mode((width, height))

# Загружаем картинку заднего фона
background = pygame.image.load('фон.png')

# Изменяем размеры
background = pygame.transform.scale(background, (width, height))

# Создаем группу спрайтов
all_sprites = pygame.sprite.Group()
enemy = Enemy()
bird=Bird()
player = Player(all_sprites)

enemy.rect.left = 200
enemy_sprites = pygame.sprite.Group()
bird_sprites=pygame.sprite.Group()
# Добавляем противника в группу спрайтов противников
enemy_sprites.add(enemy)
bird_sprites.add(bird)
bullet_sprites = pygame.sprite.Group()

# Создаем переменную FPS
FPS = 60
# Создаем объект для управления FPS
clock = pygame.time.Clock()

# Создаем шрифт
font = pygame.font.Font(None, 36)
# Создаем текст на основе шрифта
text = font.render('Жизни:' + str(player.health), True, (255, 255, 255))

text_enemy = font.render('Жизни:' + str(enemy.health), True, (255, 255, 255))


# Бесконечные игровой цикл
d=1
sound = pygame.mixer.Sound('мелодия.mp3')
sound.play()
while True:
    # Перебираем все возможные события
    for event in pygame.event.get():
        # Если произошло событие выхода из игры
        if event.type == pygame.QUIT:
            # Выходим
            exit()
        elif event.type == pygame.KEYUP:
            if d < 20:
                if event.key == pygame.K_f:
                    bullet = Bullet()
                    if player.to_right:
                        bullet.to_right = True
                        bullet.to_left = False

                        bullet.image = pygame.image.load('пуля.png')
                        bullet.image = pygame.transform.scale(bullet.image, (50, 50))
                    elif player.to_left:
                        bullet.to_left = True
                        bullet.to_right = False

                        bullet.image = pygame.image.load('пуля2.png')
                        bullet.image = pygame.transform.scale(bullet.image, (50, 50))
                    bullet_sprites.add(bullet)
    d+=1
    if d == 60:
        d = 1
    # Заливаем окно белым цветом
    win.fill((255, 255, 255))
    text = font.render('Жизни:' + str(player.health), True, (255, 0, 0))
    text_enemy = font.render('Жизни:' + str(enemy.health), True, (150, 79, 7))
    # Рисуем картинку заднего фона
    win.blit(background, (0, 0))

    # Рисуем текст
    win.blit(text, (0, 0))
    win.blit(text_enemy, (width-130,0))
    # Рисуем группу спрайтов

    all_sprites.draw(win)
    # Обновляем каждый спрайт в группе
    all_sprites.update()

    # Рисуем группу спрайтов


    enemy_sprites.draw(win)
    enemy_sprites.update()
    bullet_sprites.draw(win)
    bullet_sprites.update()
    bird_sprites.draw(win)
    bird_sprites.update()
    # Получаем столкновения(список спрайтов, с которыми столкнулся персонаж)
    hits = pygame.sprite.spritecollide(player,enemy_sprites, False)
    # Если этот список не пустой
    if len(hits) > 0:
        player.health-=1
        hits[0].rect.left = hits[0].rect.left + random.randint(300, 600)

    hits = pygame.sprite.spritecollide(enemy, bullet_sprites, False)
    # Если этот список не пустой
    if len(hits) > 0:
        enemy.health -= 1
        bullet_sprites.remove(hits[0])

    if enemy.health <=0:
        enemy.health = 5
        enemy.rect.right = width+140
    if player.health <= 0:
       break

        # Меняем координату X противника на рандомное число
        #hits[0].rect.left = random.randint(0, width - hits[0].rect.width)
        # Меняем координату Y противника на рандомное число
        #hits[0].rect.top = random.randint(0, height - hits[0].rect.height)
        #hits[0].image = pygame.image.load('1.png')

    # Обновляем окно
    pygame.display.update()
    # Настраиваем FPS
    clock.tick(FPS)