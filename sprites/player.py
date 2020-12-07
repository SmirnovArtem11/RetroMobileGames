import pygame
import os

WIDTH = 414
HEIGHT = 736

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
doodle_right_img = pygame.image.load(os.path.join(img_folder, 'doodle_right.png'))

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = doodle_right_img
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH / 2, HEIGHT / 2)
  
  
  def update(self):
    self.rect.x += 5
    if self.rect.left > WIDTH:
      self.rect.right = 0
