import pygame
import os

from settings import *

doodle_right_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_right.png')
    ), 
  (int(WIDTH/6), int(WIDTH/6/744*670))
  )

doodle_left_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_left.png')
    ), 
  (int(WIDTH/6), int(WIDTH/6/744*670))
  )

doodle_squeeze_right_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_squeeze_right.png')
    ), 
  (int(WIDTH/6), int(WIDTH/6/92*83))
  )

doodle_squeeze_left_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_squeeze_left.png')
    ), 
  (int(WIDTH/6), int(WIDTH/6/92*83))
  )

bg = pygame.image.load(os.path.join(img_folder, 'background.png'))

platform_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'platform_green.png')
    ), 
  (int(WIDTH/5), 15)
  )