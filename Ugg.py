import pygame, random
from pygame.locals import *

class Ugg():
	def __init__(self, image, posX, posY, newNextX, newNextY, whatUgg, frozen):
		self.image = image
		self.frozen = frozen
		self.x = posX
		self.y = posY
		self.nextX = newNextX
		self.nextY = newNextY
		self.Born = 0
		self.nextMOVE = 1
		self.isFalling = 0 #0 if it is not falling, 1 if he is falling from the right.
		self.leftOrRight = whatUgg #I need this attribute to understand which Ugg is. If left one or right one.
		#leftOrRight = 1 left
		#leftOrRight = 2 right
		self.speed = 1 #Default speed for Uggs.
		self.timer = pygame.time.get_ticks() + random.randint(1000,6000) #Timer for respawning uggs.

	def draw(self, screen, freeze):
		if freeze == 0:
			screen.blit(self.image, (self.x, self.y))
		elif freeze == 1:
			screen.blit(self.frozen, (self.x, self.y))
		
	def uggBorn(self, cube, value):
		if self.x < self.nextX: #left ugg.
			self.x += 35
		elif self.x > self.nextX: #right ugg.
			self.x -= 35
		elif self.x == self.nextX:
			cube.isBusy = value
			self.Born = 1 #now it's born.
			
	def animate(self):
		if self.y >= self.nextY: #if true -- bottom-up animation -- 
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
		else:					 #else -- top-down animation --
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

	def randomPath(self, indX, indY, cubeList): #note: pyramid for Ugg is a 5x5 matrix, because they fall down if they go to 0-0 or 1-1 or 2-2...6-6
		if self.x == self.nextX and self.y == self.nextY:
			while 1:
				if self.leftOrRight == 1: # ---- left Ugg! ----
					nextDecision = random.randint(0,1) #0 is top-right, 1 is bottom-right.
					if nextDecision == 0 and indX-1 >= 0 and indY < indX-1: #Right
						self.nextX += 35
						self.nextY -= 60
						cubeList[indX][indY].isBusy = 0
						return (indX-1, indY)
					elif nextDecision == 1 and indX+1 < 7: #Bottom
						self.nextX += 35
						self.nextY += 60
						cubeList[indX][indY].isBusy = 0
						return (indX+1, indY+1)
					elif nextDecision == 0 and indX-1 < 0 or indY >= indX-1:  #if he is falling down from the right (he can't fall down from bottom):
						self.isFalling = 1
						self.nextX, self.nextY = self.x+400, self.y
						cubeList[indX][indY].isBusy = 0
						return (indX, indY)
				elif self.leftOrRight == 2: # ---- right ugg! ----
					nextDecision = random.randint(0,1) #0 is top-left, 1 is bottom-left.
					if nextDecision == 0 and indY-1 > 0: #Top
						self.nextX -= 35
						self.nextY -= 60
						cubeList[indX][indY].isBusy = 0
						return (indX-1, indY-1)
					elif nextDecision == 1 and indX+1 < 7: #Left
						self.nextX -= 35
						self.nextY += 60
						cubeList[indX][indY].isBusy = 0
						return (indX+1, indY)
					elif nextDecision == 0 and indY-1 <= 0:  #If he is falling down from the top-left (he can't fall down from bottom):
						self.isFalling = 1
						self.nextX, self.nextY = self.x-400, self.y
						cubeList[indX][indY].isBusy = 0
						return (indX, indY)
		else: #This else is important because I need to wait that the animation is ended. I need to return something inside my index variables while I wait.
			return (indX, indY)
