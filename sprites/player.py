import pygame
import os

WIDTH = 414
HEIGHT = 736

game_folder = os.path.dirname(__file__)
game_folder = os.path.normpath(game_folder + os.sep + os.pardir)
img_folder = os.path.join(game_folder, 'img')

doodle_right_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_right.png')
    ), 
  (int(WIDTH/6), int(HEIGHT/12.5))
  )

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = doodle_right_img
    self.rect = self.image.get_rect()
    self.size = self.image.get_size()
    self.width = self.size[0] 
    self.height = self.size[1] 
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT
    self.speedx = 0;
  
  def update(self):
    self.rect.x += self.speedx
    
    if self.rect.left > (WIDTH - self.width/4):
      self.rect.left = -self.width*3/4
    
    if self.rect.left < (-self.width*3/4) :
      self.rect.left = WIDTH - self.width/4
