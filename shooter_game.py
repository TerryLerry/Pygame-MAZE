#Создай собственный Шутер!
#создание классов

from pygame import *
mixer.init()
from random import randint
font.init()
#создание классов
lost = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, p_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()   
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 730:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 530:
            self.rect.y = 0
            self.rect.x = randint(0,700)  
            lost = lost + 1  
            fall.play    
#создание окна игры

window = display.set_mode((800,600))
display.set_caption('Shooter')
background = transform.scale(image.load('galaxy.jpg'),(800,600)) 

#создание спрайтов
font = font.Font(None,80)

player = Player('rocket.png', 70, 530, 5)
enemy = Enemy('ufo.png',170,  0, 1)
enemy_2 = Enemy('asteroid.png', 250, 0, 2.5 )
enemy_3 = Enemy('ufo.png',370,  0, 1)
enemy_4 = Enemy('ufo.png',410,  0, 1)
enemy_5 = Enemy('asteroid.png', 650, 0, 2.5 )
monsters = sprite.Group()
monsters.add(enemy)
monsters.add(enemy_2)
monsters.add(enemy_3)
monsters.add(enemy_4)
monsters.add(enemy_5)
#создание музыки

mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')
fall = mixer.Sound('Sound_16566.ogg')

clock = time.Clock()
FPS =60

#цикл игры

game = True
while game:
    window.blit(background,(0,0))
    schet = font.render('Пропущенно:' + str(lost), True, (255,215,20))
#действия спрайтов

    player.reset()
    player.update()
    monsters.draw(window)
    monsters.update()
    window.blit(schet, (20,20))
#завершение и обновление

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()