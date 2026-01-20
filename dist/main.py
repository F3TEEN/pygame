from pygame import *
from random import *
main = 500
window_size = (700, 500)
window = display.set_mode(window_size)
background = image.load('background.webp')
background = transform.scale(background, window_size)
watch = time.Clock()
class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

       self.catcher = False
       
   def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        if self.catcher:
           draw.rect(window, (255, 0, 0), self.rect, 3)
        

#создать объект класса GameSprite
sprite1 = GameSprite('Sprite.png', 500, 300, 5)
sprite2 = GameSprite('Sprite1.png', 300, 150, 5)
choice((sprite1, sprite2)).catcher = True

while True:
    window.blit(background, (0, 0))
    sprite2.reset()
    sprite1.reset()
    press_keys = key.get_pressed()
    if press_keys[K_a]:
        if sprite1.rect.x > 0:
            sprite1.rect.x -= 5
    if press_keys[K_d]:
        if sprite1.rect.x < 650:
            sprite1.rect.x += 5    
    if press_keys[K_w]:
        if sprite1.rect.y > 0:
            sprite1.rect.y -= 5
    if press_keys[K_s]:
        if sprite1.rect.y < 445:
            sprite1.rect.y += 5
    if press_keys[K_LEFT]:
         if sprite2.rect.x > 0:
            sprite2.rect.x -= 5
    if press_keys[K_RIGHT]:
        if sprite2.rect.x < 650:
            sprite2.rect.x += 5
    if press_keys[K_UP]:
        if sprite2.rect.y > 0:
            sprite2.rect.y -= 5
    if press_keys[K_DOWN]:
        if sprite2.rect.y < 445:
            sprite2.rect.y += 5
    if sprite1.rect.colliderect(sprite2.rect):
        sprite1.catcher, sprite2.catcher = sprite2.catcher, sprite1.catcher
    
    for e in event.get():
        if e.type == QUIT:
            exit()
    display.update()
    watch.tick(120)

    