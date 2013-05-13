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
ball2 = Ball()
all = pygame.sprite.RenderUpdates()
all.add(ball)
all.add(ball2)

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
	if keys_pressed[K_UP]:
		ball.point_in_direction(90)
		ball.move(5)
	if keys_pressed[K_DOWN]:
		ball.point_in_direction(270)
		ball.move(5)
	if keys_pressed[K_l]:
		ball2.point_in_direction(180)
		ball2.move(5)
	if keys_pressed[K_h]:
		ball2.point_in_direction(0)
		ball2.move(5)
	if keys_pressed[K_k]:
		ball2.point_in_direction(90)
		ball2.move(5)
	if keys_pressed[K_j]:
		ball2.point_in_direction(270)
		ball2.move(5)

	all.clear(screen, background)

	dirty = all.draw(screen)
	pygame.display.update(dirty)
