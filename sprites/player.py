import pygame
import os

WIDTH = 414
HEIGHT = 736

game_folder = os.path.dirname(__file__)
game_folder = os.path.normpath(game_folder + os.sep + os.pardir)
img_folder = os.path.join(game_folder, 'img')

doodle_right_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_right.png')
    ), 
  (int(WIDTH/6), int(HEIGHT/12.5))
  )

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
