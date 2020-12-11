import pygame

from settings import *
from img.images import *

class LooseScreen(pygame.sprite.Sprite):
  def __init__(self, player):
    pygame.sprite.Sprite.__init__(self)
    self.image = ragged_bottom_img
    self.rect = self.image.get_rect()
    self.rect.bottom = HEIGHT + 2 + self.rect.height
    
    self.player = player
    self.is_loose = False
    
    self.speed_y = 0
  
  def update(self):
    if self.player.is_loose and not self.player.is_scrolling_up and not self.is_loose:
      self.is_loose = True
    
    if self.is_loose:
      self.scroll_up()
  
  def draw(self, screen):
    black_surface = pygame.Surface((self.rect.width, self.rect.height))
    rect = black_surface.get_rect()
    rect.bottomleft = (0, self.rect.bottom)
    black_surface.fill((0,0,0))
    screen.blit(black_surface, rect)
    
    screen.blit(self.image, self.rect)
  
  def scroll_up(self):
    if not self.rect.bottom <= (HEIGHT + 2):
      if self.rect.bottom - self.speed_y < (HEIGHT + 2):
        self.rect.bottom = HEIGHT + 2
      else:
        self.rect.bottom -= self.speed_y
        self.speed_y += abs(self.player.gravity)