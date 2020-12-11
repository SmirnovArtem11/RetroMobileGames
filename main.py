import pygame

from settings import *
from img.images import *

from sprites.player import Player
from sprites.platforms import Platforms
from sprites.score import Score
from sprites.loose_screen import LooseScreen


# init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()
running = True


# init sprites
all_sprites = pygame.sprite.Group()

player = Player()
platforms = Platforms(player)
score = Score(player, platforms.platforms[0])
loose_screen = LooseScreen(player)

for platform in platforms.platforms:
  all_sprites.add(platform)
all_sprites.add(score)
all_sprites.add(player)


def handle_events():
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

def draw():
  screen.blit(bg, (0, 0))
  
  loose_screen.draw(screen)
  all_sprites.draw(screen)
  score.draw(screen)
  
  pygame.display.flip()

def update():
  all_sprites.update()
  platforms.update()
  loose_screen.update()


while running:
  clock.tick(FPS)
  handle_events()
  update()
  draw()

pygame.quit()
