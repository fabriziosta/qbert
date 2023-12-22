import pygame, random
from pygame.locals import *
from sys import exit

class Sam():
	def __init__(self, posX, posY, newNextX, newNextY):
		self.image = pygame.image.load('Images/QB_Sam.png') #Loading Sam image.
		self.frozen = pygame.image.load('Images/QB_Sam_Frozen.png') #Loading frozen Sam image.
		self.x = posX
		self.y = posY
		self.nextX = newNextX
		self.nextY = newNextY
		self.Born = 0
		self.nextMOVE = 1
		self.speed = 1 #Default speed for sam.
		self.timer = pygame.time.get_ticks() + random.randint(1000,6000) #Timer for respawning Sam.
		
	def draw(self, screen, freeze):
		if freeze == 0:
			screen.blit(self.image, (self.x, self.y))
		elif freeze == 1:
			screen.blit(self.frozen, (self.x, self.y))

	def samBorn(self, cube, value):
		if self.y != self.nextY:
			self.y += 35
		elif self.y == self.nextY:
			cube.isBusy = value
			self.Born = 1 #Now it's born.
			
	def animate(self):
		if self.y >= self.nextY: #If true bottom-up animation.
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
		else:					 #top-down animation.
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
					
	def samRandomPath(self, indX, indY, cubeList):
		if self.x == self.nextX and self.y == self.nextY:
			while 1:
				nextDecision = random.randint(0,3) #0 is bottom-left, 1 is bottom-right, 2 top-right, 3 top-left.
				if nextDecision == 0 and indX+1 < 7: #Left
					self.nextX -= 35
					self.nextY += 60
					return (indX+1, indY)
				elif nextDecision == 1 and indX+1 < 7: #Bottom
					self.nextX += 35
					self.nextY += 60
					return (indX+1, indY+1)
				elif nextDecision == 2 and indX-1 >= 0 and len(cubeList[indX-1]) > indY: #Right
					self.nextX += 35
					self.nextY -= 60
					return (indX-1, indY)
				elif nextDecision == 3 and indX-1 >= 0 and indY-1 >= 0: #Top
					self.nextX -= 35
					self.nextY -= 60
					return (indX-1, indY-1)
		else:
			return (indX, indY)
