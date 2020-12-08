import pygame

from settings import *

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
    
    self.speed_x = 0;
    
    self.max_speed_y = 10
    self.speed_y = 10
    self.gravity = ((3*self.height - self.max_speed_y*FPS/2)*2)/((FPS/2)**2)
  
  def update(self):
    self.move_x()
    self.jump()
  
  def move_x(self):
    self.rect.x += self.speed_x
    
    if self.rect.left > (WIDTH - self.width/4):
      self.rect.left = -self.width*3/4
    
    if self.rect.left < (-self.width*3/4) :
      self.rect.left = WIDTH - self.width/4
  
  def jump(self): 
    self.rect.bottom -= self.speed_y
    self.speed_y = self.speed_y + self.gravity
    
    if self.rect.bottom >= HEIGHT: 
      self.speed_y = self.max_speed_y
  