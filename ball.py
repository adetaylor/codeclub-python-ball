#######################################################################################
# CodeClub Ball exercise
#######################################################################################

import pygame
from pygame.locals import *
import codeclub_pygame_handy_functions

pygame.init()

screen_rect = Rect(0, 0, 640, 480)
screen = pygame.display.set_mode(screen_rect.size)
ball_image = codeclub_pygame_handy_functions.load_image_from_data_directory('ball.png')
small_ball_image = pygame.transform.scale(ball_image, (50, 50))

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super(Ball, self).__init__()
        self.image = small_ball_image
        self.rect = self.image.get_rect(midbottom=screen_rect.midbottom)

    def move(self, direction, directionUD):
        self.rect.move_ip(direction*5, directionUD*5)
        self.rect = self.rect.clamp(screen_rect)

background = pygame.Surface(screen_rect.size)
ball = Ball()
all = pygame.sprite.RenderUpdates()
all.add(ball)

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
    keys_pressed = pygame.key.get_pressed()
    direction = keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]
    directionUD = keys_pressed[K_DOWN] - keys_pressed[K_UP]

    ball.move(direction, directionUD);

    all.clear(screen, background)

    dirty = all.draw(screen)
    pygame.display.update(dirty)
