import pygame, random
from pygame.locals import *
from sys import exit

class Ball():
	def __init__(self, image, posX, posY, newNextX, newNextY, greenOrRedBall):
		self.image = image
		self.x = posX
		self.y = posY
		self.nextX = newNextX
		self.nextY = newNextY
		self.isBorn = 0
		self.nextMOVE = 1
		self.greenOrRed = greenOrRedBall
		#greenOrRed = 1 RED BALL
		#greenOrRed = 2 GREEN BALL
		if self.greenOrRed == 1:
			self.frozen = pygame.image.load('Images/QB_Ball_Red_Frozen.png') #frozen ball
		self.speed = 1 #default speed for balls. It becomes "5" in the 3rd level, the most difficult.
		self.timer = pygame.time.get_ticks() + random.randint(1000,6000) #timer for respawning balls.
	
	def draw(self, screen, freeze):
		if self.greenOrRed == 2:
			screen.blit(self.image, (self.x, self.y))
		elif self.greenOrRed == 1 and freeze == 0:
			screen.blit(self.image, (self.x, self.y))
		elif self.greenOrRed == 1 and freeze == 1:
			screen.blit(self.frozen, (self.x, self.y))

	def Born(self, cube, value):
		if self.y != self.nextY:
			self.y += 35
		elif self.y == self.nextY:
			cube.isBusy = value
			self.isBorn = 1 #now it's born.
			
	def animation(self, lvl):
		if lvl == 3:
			self.speed = 5
		
		if self.y >= self.nextY: #if true bottom-up animation
			if self.y != self.nextY:
				if self.y - self.nextY > 0:
					self.y -= self.speed
				else:
					self.y += self.speed
			elif  self.y == self.nextY and self.x != self.nextX:
				if self.x - self.nextX > 0:
					self.x -= self.speed
				else:
					self.x += self.speed
		else:					 #top-down animation
			if self.x != self.nextX:
				if self.x - self.nextX > 0:
					self.x -= self.speed
				else:
					self.x += self.speed
			elif  self.x == self.nextX and self.y != self.nextY:
				if self.y - self.nextY > 0:
					self.y -= self.speed
				else:
					self.y += self.speed
					
	def RandomPath(self, indX, indY, cubeList):
		if self.x == self.nextX and self.y == self.nextY:
			nextDecision = random.randint(0,1) #0 is bottom-left, 1 is bottom-right.
			if nextDecision == 0 and indX+1 < 7: #SX
				self.nextX -= 35
				self.nextY += 60
				cubeList[indX][indY].isBusy = 0
				return (indX+1, indY)
			elif nextDecision == 1 and indX+1 < 7: #ST
				self.nextX += 35
				self.nextY += 60
				cubeList[indX][indY].isBusy = 0
				return (indX+1, indY+1)
			else:
				self.nextX, self.nextY = self.x, self.y +150
				cubeList[indX][indY].isBusy = 0
				return (indX, indY)
		else:
			return (indX, indY)
