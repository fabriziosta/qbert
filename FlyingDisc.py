import pygame
from pygame.locals import *

class FlyingDisc():
	def __init__(self, posX, posY, leftOrRight):
		self.image = pygame.image.load('Images/Disc.png') #Loading disc image.
		self.image2 = pygame.image.load('Images/Disc2.png') #Loading disc image 2.
		self.x = posX
		self.y = posY
		self.nextX = posX
		self.nextY = posY
		self.animation = 1
		self.activated = 0 #It can be used once per level. If it becomes "1" is used and disappear from the game.
		self.leftOrRight = leftOrRight
		#leftOrRight == 1: left Disc
		#leftOrRight == 2: right Disc
		
	def draw(self, screen):
		if self.activated == 0 and self.animation == 0:
			screen.blit(self.image,(self.x, self.y))
		elif self.activated == 0 and self.animation == 1:
			screen.blit(self.image2,(self.x, self.y))

	def flyingAnimation(self):
		if self.y != self.nextY:
			if self.y - self.nextY > 0:
				self.y -= 5
			else:
				self.y += 5
		elif  self.y == self.nextY and self.x != self.nextX:
			if self.x - self.nextX > 0:
				self.x -= 5
			else:
				self.x += 5
