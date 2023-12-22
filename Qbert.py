import pygame
from pygame.locals import *
from sys import exit

ORANGE = (255, 165, 0)

class Qbert():
	def __init__(self, lives, posX, posY):
		self.lives = lives
		self.imageToBlit = pygame.image.load('Images/qbert.png') #Loading Q*bert image.
		self.image = pygame.image.load('Images/qbert.png') #Loading Q*bert image.
		self.imageInverse = pygame.image.load('Images/qbert_inverse.png') #Loading reverse Q*bert image.
		self.lifeImage = pygame.image.load('Images/lives.png') #Loading life image.
		self.x = posX
		self.y = posY
		self.nextX = posX
		self.nextY = posY
		self.nextMOVE = True #You can't continue to pick keydown events until animation isn't over. It disable MultipleKeydown Events too.
		self.speed = 5 #Q*bert's speed for 1 FPS.
		self.endAnimation = False #I need this boolean variable to check if Qbert animation is ended. If it is ended, draw and update cubes.
		
	def draw(self, screen):
		screen.blit(self.imageToBlit,(self.x, self.y))
		
	def animation(self):
		if self.y >= self.nextY: #If true bottom-up animation
			if self.y != self.nextY:
				self.nextMOVE = False
				if self.y - self.nextY > 0:
					self.y -= self.speed
				else:
					self.y += self.speed
			elif  self.y == self.nextY and self.x != self.nextX:
				if self.x - self.nextX > 0:
					self.x -= self.speed
				else:
					self.x += self.speed
			else:
				self.nextMOVE = True
				
		else:					 #Else top-down animation
			if self.x != self.nextX:
				self.nextMOVE = False
				if self.x - self.nextX > 0:
					self.x -= self.speed
				else:
					self.x += self.speed
			elif  self.x == self.nextX and self.y != self.nextY:
				if self.y - self.nextY > 0:
					self.y -= self.speed
				else:
					self.y += self.speed
			else:
				self.nextMOVE = True
		
	def drawLives(self, screen):
		if self.lives == 1:
			screen.blit(self.lifeImage,(10,140))
		elif self.lives == 2:
			screen.blit(self.lifeImage,(10,140))
			screen.blit(self.lifeImage,(10,170))
		elif self.lives == 3:
			screen.blit(self.lifeImage,(10,140))
			screen.blit(self.lifeImage,(10,170))
			screen.blit(self.lifeImage,(10,200))
		elif self.lives == 4:
			screen.blit(self.lifeImage,(10,140))
			screen.blit(self.lifeImage,(10,170))
			screen.blit(self.lifeImage,(10,200))
			screen.blit(self.lifeImage,(10,230))
	
	def isDead(self, screen):
		while 1:
			screen.blit(pygame.font.Font ('freesansbold.ttf', 50).render('You lost a life.', 1, ORANGE),(165, 300))
			screen.blit(pygame.font.Font ('freesansbold.ttf', 40).render('PRESS SPACE TO CONTINUE', 1, ORANGE),(35, 350))
			
			if pygame.key.get_pressed()[pygame.K_SPACE]: 
				return False
			if pygame.event.get(pygame.QUIT): return
			pygame.display.update()

	def jumpOnDisc(self, numDisc):
		if numDisc == 2:
			self.nextX = 500
			self.nextY = 330
		elif numDisc == 1:
			self.nextX = 120
			self.nextY = 330
