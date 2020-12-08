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
  
  def update(self): 
    if self.player.is_falling:
      if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.right and self.player.rect.bottom > self.rect.top and self.player.rect.bottom < self.rect.centery:
        self.player.start_jump()


class Platforms(pygame.sprite.Sprite):
  def __init__(self, player):
    pygame.sprite.Sprite.__init__(self)
    self.platforms = []
    
    for y in range (HEIGHT - 150, -2*HEIGHT, -150):
      platform = Platform(WIDTH/2, y, player)
      self.platforms.append(platform)
