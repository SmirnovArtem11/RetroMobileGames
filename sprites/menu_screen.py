import pygame

from settings import *
from img.images import *
from sound.sounds import *

class Menu(pygame.sprite.Sprite):
  def __init__(self, screen_manager):
    pygame.sprite.Sprite.__init__(self)
    self.image = doodle_logo_img
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH/2, HEIGHT/3)
    
    self.play_img = play_img
    self.rect_play = self.play_img.get_rect()
    self.rect_play.center = (WIDTH/2, HEIGHT/3*2)

    self.screen_manager = screen_manager
  
  def draw(self, screen):
    screen.blit(self.image, self.rect)
    screen.blit(self.play_img, self.rect_play)
  
  def on_click(self, mouse_pos):
    x, y = mouse_pos
    if y < self.rect_play.bottom and y > self.rect_play.top and x < self.rect_play.right and x > self.rect_play.left:
      self.screen_manager.start_game()
  