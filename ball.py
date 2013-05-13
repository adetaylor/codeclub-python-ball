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
	if keys_pressed[K_RIGHT]:
		ball.point_in_direction(180)
		ball.move(5)
	if keys_pressed[K_LEFT]:
		ball.point_in_direction(0)
		ball.move(5)

	all.clear(screen, background)

	dirty = all.draw(screen)
	pygame.display.update(dirty)
