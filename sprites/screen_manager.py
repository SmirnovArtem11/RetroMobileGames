import pygame

from settings import *
from img.images import *
from sound.sounds import *

class ScreenManager(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    
    self.is_game_start = False
  
  def start_game(self):
    self.is_game_start = True