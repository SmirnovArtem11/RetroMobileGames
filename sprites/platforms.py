import pygame
import random

from settings import *
from img.images import *

class Platform(pygame.sprite.Sprite):
  def __init__(self, x, y, player):
    pygame.sprite.Sprite.__init__(self)
    self.image = platform_img
    self.rect = self.image.get_rect()
    self.rect.left = x
    self.rect.top = y
    
    self.player = player
    
    self.speed_y = 0
    self.is_scrolling_down = False
    self.is_scrolling_up = False
  
  def update(self): 
    if self.player.is_falling:
      if len(pygame.sprite.spritecollide(self.player, [self], False)) and self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.right and self.player.rect.bottom > self.rect.top and self.player.rect.bottom < self.rect.bottom:
        self.player.start_jump()
    
    if self.player.rect.top < HEIGHT/2 and not self.is_scrolling_down and not self.player.is_falling:
      self.start_scroll_down()
    
    if self.is_scrolling_down:
      self.scroll_down()
    
    if self.is_scrolling_up:
      self.scroll_up()
    
    self.move_x()

  def start_scroll_down(self):
    self.player.is_stop = True
    self.is_scrolling_down = True
    self.speed_y = self.player.speed_y

  def scroll_down(self):
    if self.is_scrolling_down:
      if self.speed_y <= 0:
        self.is_scrolling_down = False
        
        self.player.speed_y = 0
        self.player.is_stop = False
        return
      
      self.rect.bottom += self.speed_y
      self.speed_y = self.speed_y + self.player.gravity
  
  def start_scroll_up(self):
    self.is_scrolling_up = True
    self.speed_y = abs(self.player.speed_y)
  
  def scroll_up(self):
    if self.is_scrolling_up:
      self.rect.bottom -= self.speed_y
      self.speed_y = self.speed_y + abs(self.player.gravity)
  
  def end_game(self):
    self.start_scroll_up()
  
  def move_x(self):
    pass


class GreenPlatform(Platform):
  def __init__(self, x, y, player):
    Platform.__init__(self, x, y, player)
    self.image = platform_img


class BluePlatform(Platform):
  def __init__(self, x, y, player):
    Platform.__init__(self, x, y, player)
    self.image = platform_blue_img
    self.default_speed_x = 4
    self.current_speed_x = 4
  
  def move_x(self):
    if self.current_speed_x > 0:
      if self.rect.right + self.current_speed_x >= WIDTH:
        self.rect.right = WIDTH
        self.current_speed_x = -self.default_speed_x
      else:
        self.rect.right += self.current_speed_x
    else: 
      if self.rect.left + self.current_speed_x <= 0:
        self.rect.left = 0
        self.current_speed_x = self.default_speed_x
      else:
        self.rect.left += self.current_speed_x


class Platforms(pygame.sprite.Sprite):
  def __init__(self, player):
    pygame.sprite.Sprite.__init__(self)
    self.platforms = []
    self.player = player
    
    self.is_loose = False
    
    lowestPlatform = GreenPlatform(-500, HEIGHT-platform_size[1], player)
    self.platforms.append(lowestPlatform)
    self.new_platforms = []
    
    self.generate_platforms()
  
  def update(self):
    if self.player.is_loose and not self.is_loose:
      self.end_game()
    
    if not self.player.is_loose and self.is_loose:
      self.play_again()

    self.kill_platforms()
  
  def kill_platforms(self):
    for platform in self.platforms[1:]:
      if platform.rect.top > HEIGHT:
        platform.kill()
  
  def end_game(self):
    self.is_loose = True
    
    for platform in self.platforms[1:]:
      platform.end_game()
  
  def generate_platforms(self):
    current_h = HEIGHT
    for i in range (500):
      x = random.randint(0, WIDTH - platform_size[0])
      y = current_h - random.randint(35, self.player.rect.height*3)
      current_h = y
      if random.random() > 0.4: 
        platform = GreenPlatform(x, y, self.player)
      else:
        platform = BluePlatform(x, y, self.player)
      self.platforms.append(platform)
  
  def play_again(self):
    self.is_loose = False
    
    for platform in self.platforms[1:]:
      platform.kill()
    
    self.platforms[0].rect.bottom = HEIGHT-platform_size[1]
    self.platforms = [self.platforms[0]]
    
    self.generate_platforms()
    
    self.new_platforms = self.platforms[1:]
    
  def append_new_platforms(self, all_sprites):
    if len(self.new_platforms) > 0:
      for platform in self.new_platforms:
        all_sprites.add(platform)
    
    self.new_platforms = []
    return all_sprites