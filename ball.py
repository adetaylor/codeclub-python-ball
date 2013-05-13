#######################################################################################
# CodeClub Ball exercise
#######################################################################################

import pygame
from pygame.locals import *
import codeclub

pygame.init()

screen_rect = Rect(0, 0, 640, 480)
screen = pygame.display.set_mode(screen_rect.size)

class Ball(codeclub.CodeClubSprite):

	def __init__(self):
		super(Ball, self).__init__()
		self.set_costume('ball.png', 50)

	def move_in_direction(self, direction):
		self.rect.move_ip(direction*5, 0)
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

	ball.move_in_direction(direction);

	all.clear(screen, background)

	dirty = all.draw(screen)
	pygame.display.update(dirty)
