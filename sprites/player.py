import pygame
import os

from settings import *

from img.images import *

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
    
    self.default_speed_x = 8;
    self.speed_x = 0;
    self.is_right = True
    
    self.default_speed_y = 10
    self.speed_y = 10
    self.gravity = ((3*self.height - self.default_speed_y*FPS/2)*2)/((FPS/2)**2)
    self.is_squezing = False
  
  def update(self):
    self.move_x()
    self.jump()
  
  def start_move_x(self, speed):
    self.speed_x = speed
    
    if self.is_squezing:
      if speed > 0:
        self.image = doodle_squeeze_right_img
        self.is_right = True
      elif speed < 0:
        self.image = doodle_squeeze_left_img
        self.is_right = False
    else:
      if speed < 0:
        self.image = doodle_left_img
        self.is_right = False
      elif speed > 0:
        self.image = doodle_right_img
        self.is_right = True
  
  def move_x(self):
    self.rect.x += self.speed_x
    
    if self.rect.left > (WIDTH - self.width/4):
      self.rect.left = -self.width*3/4
    
    if self.rect.left < (-self.width*3/4) :
      self.rect.left = WIDTH - self.width/4

  def start_jump(self):
    self.speed_y = self.default_speed_y

    self.is_squezing = True
    
    if self.is_right:
      self.image = doodle_squeeze_right_img
    else:
      self.image = doodle_squeeze_left_img
    
    pygame.time.set_timer(JUMPEVENT, 200, True)
  
  def un_squeeze(self):
    self.is_squezing = False
    
    if self.is_right:
      self.image = doodle_right_img
    else:
      self.image = doodle_left_img
  
  def jump(self): 
    self.rect.bottom -= self.speed_y
    self.speed_y = self.speed_y + self.gravity
    
    if self.rect.bottom >= HEIGHT: 
      self.start_jump()
  