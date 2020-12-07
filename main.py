import pygame
import os

from sprites.player import Player

WIDTH = 414
HEIGHT = 736
FPS = 60

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

bg = pygame.image.load(os.path.join(img_folder, 'background.png'))
# bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

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
  
  screen.blit(bg, (0, 0))
  all_sprites.draw(screen)
  pygame.display.flip()

pygame.quit()