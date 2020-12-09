import pygame

from settings import *
from img.images import *

font_name = "./fonts/DoodleJump.ttf"

class Score(pygame.sprite.Sprite):
  def __init__(self, player, lowest_platform):
    pygame.sprite.Sprite.__init__(self)
    self.image = top_score_img
    self.rect = self.image.get_rect()
    self.rect.topleft = (0, 0)
    
    self.player = player
    self.platform = lowest_platform 
    
    self.max_distance = 0
    self.score = 0
    self.score_by_height = 1000
  
  def update(self):
    self.calc_score()
  
  def calc_score(self):
    distance = abs(self.player.rect.bottom - self.platform.rect.top)
    if distance > self.max_distance:
      new_score = int(distance / HEIGHT * self.score_by_height)
      self.score = new_score
      self.max_distance = distance
  
  def print_score(self):
    font = pygame.font.Font(font_name, 40)
    text_surface = font.render(str(self.score), True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (20, -5)
    return (text_surface, text_rect)