from pygame import *
mixer.init()
font.init()
#создание класса
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
    def __init__(self, player_image, player_x, player_y, p_speed):
        super().__init__(player_image, player_x, player_y, p_speed)
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] :
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.speed    
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, p_speed):
        super().__init__(player_image, player_x, player_y, p_speed)
    def update(self):
        # side = 'right'
        if self.rect.x == 630:
            self.side = 'left'
        if self.rect.x == 500:
            self.side = 'right'   
        if self.side =='right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
    #def cheat_update(self):
        # side = 'right'
        #if self.rect.x == 630:
        #    self.side = 'left'
        #if self.rect.x == 500:
#self.side = 'right'   
      #  if self.side =='right':
      #      self.rect.x += 1
      #  else:
      #      self.rect.x -= 1      
                 
class Wall(sprite.Sprite):
    def __init__(self, wall_color1,wall_color2, wall_color3, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.color1 = wall_color1 
        self.color2 = wall_color2
        self.color3 = wall_color3     
        self.width = wall_width      
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((self.color1,self.color2,self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))  
#создание спрайтов
sprite_player=Player('hero.png', 100, 400, 10)   
sprite_enemy=Enemy('cyborg.png', 500, 165, 1)   
sprite_treasure = GameSprite('treasure.png', 550,420,0)    
wall_1 = Wall(192, 192, 192, 20, 500, 275, 80)  
wall_2 = Wall(192, 192, 192, 20, 420, 390, 0)  
wall_3 = Wall(192, 192, 192, 20, 400, 160, 0)  
wall_4 = Wall(192, 192, 192, 160, 20, 0, 380)  
wall_5 = Wall(192, 192, 192, 20, 500, 480, 80)  
#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(700,500))
#создание музыки
mixer.music.load('jungles.ogg')
mixer.music.play() 
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
#создание надписей
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255,215,0))
lose = font.render('YOU LOSE!', True, (255,215,0))
#сoздание переменных, связанных с циклом
clock = time.Clock()
FPS = 60
#создание цикла
game = True
finish = False
while game:
    if finish != True:
#задай фон сцены
        window.blit(background, (0,0))  
#
            
        sprite_player.update()
        sprite_player.reset() 
        sprite_enemy.reset()   
        sprite_enemy.update()      
        sprite_treasure.reset()
        wall_1.reset()
        wall_2.reset()
        wall_3.reset()
        wall_4.reset()
        wall_5.reset()
        if sprite.collide_rect(sprite_player, sprite_enemy) or sprite.collide_rect(sprite_player, wall_1) or sprite.collide_rect(sprite_player, wall_2) or sprite.collide_rect(sprite_player, wall_3) or sprite.collide_rect(sprite_player, wall_4) or sprite.collide_rect(sprite_player, wall_5):
            window.blit(lose, (200,200))
            finish = True
            kick.play()
        if sprite.collide_rect(sprite_player, sprite_treasure):
            window.blit(win, (200,200))
            finish = True
            money.play()    
#обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False
    
            
                              
#обновление fps    
    clock.tick(FPS)        
    display.update()



