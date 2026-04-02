import random
import sys
from random import randint
from time import sleep

from pygame import*

class Model(sprite.Sprite):
    def __init__(self, filename, size_x, size_y, pos_x, pos_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(Model):
    def update(self):
        coords = [[820, 100], [250, 200], [1400, 250], [1280, 570], [1000, 570], [1000, 800], [630, 800], [630, 570]]
        random_coord = random.choice(coords)
        sleep(1)
        self.rect.x = random_coord[0]
        self.rect.y = random_coord[1]

class Door(sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height, r, g, b):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.visible = True
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((1820,980))
display.set_caption('шутер')
background = transform.scale(image.load("background2.jpg"), (1820, 980))
clock = time.Clock()
enemy = Enemy('animatronic.png', 150, 100,630, 570, 2)
door1 = Door( 780, 780, 10, 100, 128, 128, 128)
door2 = Door( 980, 780, 10, 100, 128, 128, 128)
font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN!", True, (0, 200, 0))
lose = font.render("YOU LOST", True, (255, 0, 0))
gameower = False
timer = 10
while True:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            sys.exit()
        if i.type == MOUSEBUTTONDOWN:
            if i.button == 1:
                if door1.visible:
                    door1.visible = False
                else:
                    door1.visible = True
        if i.type == MOUSEBUTTONDOWN:
            if i.button == 3:
                if door2.visible:
                    door2.visible = False
                else:
                    door2.visible = True

    timer_text = font.render("Time: " + str(timer), True, (255, 255, 255))
    window.blit(timer_text, (10, 10))
    enemy.reset()
    if not gameower and timer > 0:
        enemy.update()
        timer -= 1

    if door1.visible:
        door1.reset()
    if door2.visible:
        door2.reset()

    if not door1.visible and enemy.rect.x == 1000 and enemy.rect.y == 800:
        gameower = True


    if gameower:
        window.blit(lose, (1000, 800))

    if timer <= 0:
        window.blit(win, (1000, 800))

    display.update()
    clock.tick(75)
