import pygame
import os

from settings import *
from img.images import *

from sprites.player import Player
from sprites.platforms import Platforms

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

platforms = Platforms()

for platform in platforms.platforms:
  all_sprites.add(platform)
  
running = True

while running:
  clock.tick(FPS)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        player.start_move_x(0)
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player.start_move_x(-player.default_speed_x)
      if event.key == pygame.K_RIGHT:
        player.start_move_x(player.default_speed_x)
    
    if event.type == JUMPEVENT:
      player.un_squeeze()
  
  
  all_sprites.update()
  
  screen.blit(bg, (0, 0))
  all_sprites.draw(screen)
  pygame.display.flip()

pygame.quit()