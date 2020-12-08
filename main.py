import pygame
import os

from settings import *

from sprites.player import Player

bg = pygame.image.load(os.path.join(img_folder, 'background.png'))

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
  clock.tick(FPS)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player.speed_x = -8
      if event.key == pygame.K_RIGHT:
        player.speed_x = 8
    
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        player.speed_x = 0
  
  
  all_sprites.update()
  
  screen.blit(bg, (0, 0))
  all_sprites.draw(screen)
  pygame.display.flip()

pygame.quit()