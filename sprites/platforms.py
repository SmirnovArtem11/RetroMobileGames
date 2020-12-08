import pygame
import os

from settings import *
from img.images import *

class Platform(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = platform_img
    self.rect = self.image.get_rect()
    
    self.rect.centerx = x
    self.rect.bottom = y

class Platforms(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.platforms = []
    
    for y in range (HEIGHT - 150, -2*HEIGHT, -150):
      platform = Platform(WIDTH/2, y)
      self.platforms.append(platform)
