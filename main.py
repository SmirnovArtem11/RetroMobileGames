import pygame
import random

from sprites.player import Player

WIDTH = 414
HEIGHT = 736
FPS = 60

BLACK = (0, 0, 0)

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
  
  all_sprites.update()
  
  screen.fill(BLACK)
  all_sprites.draw(screen)
  pygame.display.flip()

pygame.quit()