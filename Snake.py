import pygame
from pygame.locals import *
from sys import exit

class Snake():
	def __init__(self):
		self.ball = pygame.image.load('Images/QB_Ball_Purple.png') #Loading purple_ball image.
		self.snake = pygame.image.load('Images/old_Coily.png') #Loading snake image.
		self.snake_frozen = pygame.image.load('Images/old_Coily_Frozen.png') #Loading frozen snake image.
		self.x = 315
		self.y = -35
		self.nextX = 315 #1st cube
		self.nextY = 140 #1st cube
		self.isBall = 0
		self.snakeNextMOVE = True
		#snakeNextMOVE = False #snake is moving, don't do anything.
		#snakeNextMOVE = True #snake can move.
		self.speed = 1
		self.ItsTimeToSpawn = False #This variable is important to cast a good animation when snake born.
	
	def draw(self, screen, freeze):
		if self.isBall == 0:
			screen.blit(self.ball, (self.x, self.y))
		elif self.isBall == 1 and freeze == 0:
			screen.blit(self.snake, (self.x, self.y))
		elif self.isBall == 1 and freeze == 1:
			screen.blit(self.snake_frozen, (self.x, self.y))
		
	def snakeBorn(self):
		if self.y != self.nextY:
			self.y += 35
		elif self.y == self.nextY:
			self.isBall = 1 #Now it's ready to go on the bottom of the pyramid and follow Q*bert.
		
	def animate(self):
		if self.y >= self.nextY: #If true bottom-up animation
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
		else:					 #Top-down animation
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

	def followBert(self, indX, indY, cubeList, bertX, bertY):
		if self.x == self.nextX and self.y == self.nextY:
			if bertX <= self.x and bertY >= self.y: #Left
				self.nextX -= 35
				self.nextY += 60
				return (indX+1, indY)
			elif bertX >= self.x and bertY >= self.y: #Bottom
				self.nextX += 35
				self.nextY += 60
				return (indX+1, indY+1)
			elif bertX >= self.x and bertY <= self.y: #Right
				self.nextX += 35
				self.nextY -= 60
				return (indX-1, indY)
			elif bertX <= self.x and bertY <= self.y: #Top
				self.nextX -= 35
				self.nextY -= 60
				return (indX-1, indY-1)
		else:
			return (indX, indY)
		
#-------ALL X AND Y VALUES OF MY snake IN THE CUBES---------------#
#(315,140) #0-0          (+15, -20)

#(280,200) #1-0 
#(350,200) #1-1 

#(245,260) #2-0 
#(315,260) #2-1
#(385,260) #2-2

#(210,320) #3-0
#(280,320) #3-1
#(350,320) #3-2
#(420,320) #3-3

#(175,380) #4-0
#(245,380) #4-1
#(315,380) #4-2
#(385,380) #4-3
#(455,380) #4-4

#(140,440) #5-0
#(210,440) #5-1
#(280,440) #5-2
#(350,440) #5-3
#(420,440) #5-4
#(490,440) #5-5

#(105,500) #6-0
#(175,500) #6-1
#(245,500) #6-2
#(315,500) #6-3
#(385,500) #6-4
#(455,500) #6-5
#(525,500) #6-6
