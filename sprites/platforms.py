import pygame
import os

from settings import *
from img.images import *

class Platform(pygame.sprite.Sprite):
  def __init__(self, x, y, player):
    pygame.sprite.Sprite.__init__(self)
    self.image = platform_img
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.bottom = y
    
    self.player = player
    
    self.speed_y = 0
    self.is_scrolling = False
  
  def update(self): 
    if self.player.is_falling:
      if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.right and self.player.rect.bottom > self.rect.top and self.player.rect.bottom < self.rect.centery:
        self.player.start_jump()
    
    if self.player.rect.top < HEIGHT/2 and not self.is_scrolling and not self.player.is_falling:
      self.start_scroll()
    
    self.scroll()

  def start_scroll(self):
    self.player.is_stop = True
    self.is_scrolling = True
    self.speed_y = self.player.speed_y

  def scroll(self):
    print(self.player.rect.top)
    print(HEIGHT/2)
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
    
    for y in range (HEIGHT - 150, -2*HEIGHT, -150):
      platform = Platform(WIDTH/2, y, player)
      self.platforms.append(platform)
