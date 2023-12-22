import pygame
from pygame.locals import *
from sys import exit

pygame.init()
font = pygame.font.Font('freesansbold.ttf',24)
PURPLE = (128,0,128)
RED = (255,0,0)
GREEN = (0,128,0)
ORANGE = (255, 165, 0)

class Level():
	def __init__(self, blue, red, white):
		self.rounds = 1
		self.levels = 1
		self.score = 0
		self.extraLife = False #It becomes TRUE at 8000 points and the user receives a new life only once!
		
		self.splashScreenLvl1 = pygame.image.load('Images/lvl_up_1.png') #Splash screens!
		self.splashScreenLvl2 = pygame.image.load('Images/lvl_up_2.png')
		self.splashScreenLvl3 = pygame.image.load('Images/lvl_up_3.png')
		
		self.whiteCube = white #White cube
		self.redCube = red #Red cube
		self.blueCube = blue #Blue cube
		
	def startingPoint(self, screen): #Starting point of the game.
		screen.blit(self.splashScreenLvl1, (0, 0))
		screen.blit(pygame.font.Font ('freesansbold.ttf', 50).render('PRESS SPACE TO START', 1, GREEN),(50, 310))
		if pygame.key.get_pressed()[pygame.K_SPACE]: 
			return False
		if pygame.event.get(pygame.QUIT): return
		pygame.display.update()
		return True

	def drawLevel(self, screen):
		screen.blit(font.render('PLAYER', 1, PURPLE),(20,20))
		pygame.draw.rect(screen, RED, (130,25, 15,15), 20)
		screen.blit(font.render('1', 1, GREEN),(130,20))
		screen.blit(font.render(str(self.score), 1, ORANGE),(50,50)) #SHOWING SCORE 
		
		screen.blit(font.render('LEVEL: ', 1, GREEN),(520,120))
		screen.blit(font.render('ROUND: ', 1, PURPLE),(520,145))
		screen.blit(font.render(str(self.levels), 1, ORANGE),(620,120))
		screen.blit(font.render(str(self.rounds), 1, ORANGE),(620,145))
	
	def winRound(self, cubeList): #checkWin starts TRUE, but if only one cube is != from the one requested to win, it becomes FALSE.
		checkWin = True
		for myList in cubeList:
			for elem in myList:
				if self.levels == 1 and elem.isActive != 1 :
					checkWin = False
				elif self.levels > 1 and elem.isActive != 2 :
					checkWin = False
		if checkWin == True:
			print("WIN!!")
			return True
	
	def winAnimation(self, screen):
		while 1:
			if self.rounds < 3:
				screen.blit(pygame.font.Font ('freesansbold.ttf', 50).render('ROUND WIN! PRESS SPACE', 1, GREEN),(15, 300))
				
			elif self.rounds == 3 and self.levels == 1:
				screen.blit(self.splashScreenLvl2, (0, 0))
				screen.blit(pygame.font.Font ('freesansbold.ttf', 50).render('LEVEL WIN! PRESS SPACE', 1, ORANGE),(25, 310))
				
			elif self.rounds == 3 and self.levels == 2:
				screen.blit(self.splashScreenLvl3, (0, 0))
				screen.blit(pygame.font.Font ('freesansbold.ttf', 50).render('LEVEL WIN! PRESS SPACE', 1, PURPLE),(25, 310))
				
			elif self.rounds == 3 and self.levels == 3:
				self.winSplashScreen(screen) #USER WIN THE GAME! CONGRATULATION and GAME OVER!
						
			if pygame.key.get_pressed()[pygame.K_SPACE]: 
				if self.rounds < 3:
					self.rounds += 1
				elif self.rounds == 3 and self.levels < 3:
					self.rounds = 1
					self.levels += 1

				return False
			if pygame.event.get(pygame.QUIT): return
			pygame.display.update()
		
	def gameOver(self, screen):
		while 1:
			screen.fill((0,0,0)) #Fill screen with black
			screen.blit(pygame.font.Font ('freesansbold.ttf', 50).render('GAME OVER', 1, RED),(170, 300))
			if pygame.event.get(pygame.QUIT): return
			pygame.display.update()

	def winSplashScreen(self,screen):
		while 1:
			screen.fill((0,0,0)) #Fill screen with black
			screen.blit(pygame.font.Font ('freesansbold.ttf', 50).render('YOU WIN! GAME OVER', 1, ORANGE),(50, 300))
			if pygame.event.get(pygame.QUIT): return
			pygame.display.update()

