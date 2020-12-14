import pygame

from settings import *
from img.images import *

class PlayAgain(pygame.sprite.Sprite):
  def __init__(self, loose_screen, player):
    pygame.sprite.Sprite.__init__(self)
    self.loose_screen = loose_screen
    self.player = player
    
    self.image = play_again_img
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH/2
    self.rect.bottom = self.loose_screen.rect.bottom - 50 - 10 - ragged_bottom_size[1] 
  
  def update(self):
    self.rect.bottom = self.loose_screen.rect.bottom - 50 - 10 - ragged_bottom_size[1]
  
  def draw(self, screen):
    screen.blit(self.image, self.rect)
  
  def on_click(self, mouse_pos):
    x, y = mouse_pos
    if y < self.rect.bottom and y > self.rect.top and x < self.rect.right and x > self.rect.left:
      self.player.play_again()


class LooseScreen(pygame.sprite.Sprite):
  def __init__(self, player):
    pygame.sprite.Sprite.__init__(self)
    self.image = ragged_bottom_img
    self.rect = pygame.Rect(0, 0, 0, 0)
    
    self.rect.width = ragged_bottom_size[0]
    self.rect.height = ragged_bottom_size[1]+10+50+play_again_size[1]
    
    self.rect.top = HEIGHT
    
    self.play_again_btn = PlayAgain(self, player)
    self.player = player
    
    self.is_loose = False
    self.speed_y = 0
  
  def update(self):
    if self.player.is_loose and not self.player.is_scrolling_up and not self.is_loose:
      self.end_game()
    
    if self.is_loose:
      self.scroll_up()
    
    if self.is_loose and not self.player.is_loose:
      self.play_again()
    
    self.play_again_btn.update()
  
  def draw(self, screen):
    # draw black rectangle
    black_surface = pygame.Surface((ragged_bottom_size[0], ragged_bottom_size[1]))
    black_surface.fill((0,0,0))
    screen.blit(black_surface, (0, self.rect.bottom - ragged_bottom_size[1]))
    
    # draw ragged paper
    screen.blit(self.image, (0, self.rect.bottom - ragged_bottom_size[1]-10))
    
    self.play_again_btn.draw(screen)
  
  def scroll_up(self):
    if not self.rect.bottom <= HEIGHT:
      if self.rect.bottom - self.speed_y < HEIGHT:
        self.rect.bottom = HEIGHT
      else:
        self.rect.bottom -= self.speed_y
        self.speed_y += abs(self.player.gravity)

  def on_click(self, mouse_pos):
    self.play_again_btn.on_click(mouse_pos)
  
  def end_game(self):
    self.is_loose = True
  
  def play_again(self):
    self.rect.top = HEIGHT
    self.is_loose = False
    self.speed_y = 0