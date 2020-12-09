import pygame
import random

from settings import *
from img.images import *

class Platform(pygame.sprite.Sprite):
  def __init__(self, x, y, player):
    pygame.sprite.Sprite.__init__(self)
    self.image = platform_img
    self.rect = self.image.get_rect()
    self.rect.left = x
    self.rect.top = y
    
    self.player = player
    
    self.speed_y = 0
    self.is_scrolling = False
  
  def update(self): 
    if self.player.is_falling:
      #доделать
      if len(pygame.sprite.spritecollide(self.player, [self], False)) and self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.right and self.player.rect.bottom > self.rect.top and self.player.rect.bottom < self.rect.bottom:
        self.player.start_jump()
    
    if self.player.rect.top < HEIGHT/2 and not self.is_scrolling and not self.player.is_falling:
      self.start_scroll()
    
    self.scroll()

  def start_scroll(self):
    self.player.is_stop = True
    self.is_scrolling = True
    self.speed_y = self.player.speed_y

  def scroll(self):
    if self.is_scrolling:
      if self.speed_y <= 0:
        self.is_scrolling = False
        
        self.player.speed_y = 0
        self.player.is_stop = False
        return
      
      self.rect.bottom += self.speed_y
      self.speed_y = self.speed_y + self.player.gravity
  

class Platforms(pygame.sprite.Sprite):
  def __init__(self, player):
    pygame.sprite.Sprite.__init__(self)
    self.platforms = []
    
    lowestPlatform = Platform(-500, HEIGHT-10, player)
    self.platforms.append(lowestPlatform)
    
    current_h = HEIGHT
    for i in range (1000):
      x = random.randint(0, int(4/5*WIDTH))
      y = current_h - random.randint(35, player.rect.height*3)
      current_h = y
      
      platform = Platform(x, y, player)
      self.platforms.append(platform)
    
