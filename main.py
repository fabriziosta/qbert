import pygame, sys, random
from pygame.locals import *
from sys import exit

#Classes
from Qbert import *
from Snake import *
from Ball import *
from Ugg import *
from FlyingDisc import *
from Level import *
from Cube import *
from Sam import *

pygame.init()
BLACK = (0,0,0) #colors!
WHITE = (255,255,255)
PURPLE = (128,0,128)
RED = (255,0,0)
GREEN = (0,128,0)
ORANGE = (255, 165, 0)

def findSprite(l, value): #Find a sprite on the cubes checking the "isBusy" attribute of the cubes. 
	for z in range(0,7):
		for i in range(0, z+1):
			if l[z][i].isBusy == value:
				l[z][i].isBusy = 0
				return (z, i)

def resetCubes(cubeList): #Resetting cubes and everything when Qbert dies, collides with enemies, win or fall down.
	for myList in cubeList: #Every round, every level, I have to put all cubes on white color.
		for elem in myList:
			elem.isBusy = 0
			elem.isActive = 0
	return cubeList

#0.0 Basic configurations.
FPS = 60 #fps of my game
start = True #It becomes true when user press SPACE key to start the game.

win = False #This becomes true when user win a level.
#win == True means user has win round/level.
#win == False means user has not win yet.

dead = False 
#dead == False means Qbert is not dead.
#dead == True means Qbert fall down or he collides with enemies.

freeze = 0 #If this variable becomes 1, all enemies must freeze.
timerFreezing = 0 #I'll save inside this variable the actual timer when qbert catch the green ball. After 3 secs enemies will lost the freezing effect.

RESET = False 
#RESET == False means that there isn't need to reset the game.
#RESET == True means that qbert dies or user wins and I have to reset all the GUI and the game!

newX, newY = 0, 0 #this indexes will be used to save the indexes of the keydown the user pressed. After the animation has ended, the number "1" will be written inside cubeList.isBusy.

#1.0 Creating window
screen = pygame.display.set_mode((700, 650))
pygame.display.set_caption('SupQ*Bert')

#2.0 Loading all the images 
cubeImg = pygame.image.load('Images/cube.png') #Loading WHITE cube image.
blue_cubeImg = pygame.image.load('Images/spr_cube_blue.png') #Loading BLUE cube image.
red_cubeImg = pygame.image.load('Images/spr_cube_red.png') #Loading RED cube image.

uggLeft = pygame.image.load('Images/UggLeft.png') #Loading Ugg left one.
uggRight = pygame.image.load('Images/UggRight.png') #Loading Ugg right one.
uggLeft_frozen = pygame.image.load('Images/UggLeft_Frozen.png') #Loading Ugg right frozen.
uggRight_frozen = pygame.image.load('Images/UggRight_Frozen.png') #Loading Ugg right frozen.

redBall = pygame.image.load('Images/QB_Ball_Red.png') #Loading red_ball.
redBall_frozen = pygame.image.load('Images/QB_Ball_Red_Frozen.png') #Loading frozen red_ball.
greenBall = pygame.image.load('Images/QB_Ball_Green.png') #Loading green_ball.

#3.0 Set up music - # Start Music   
music = pygame.mixer.music.load("Sound/qbert.mp3")
pygame.mixer.music.play(-1)

#4.0 Initialize my 28 cubes objects and add them inside a list.
cubeList = [[None]*i for i in range(1,8)]
cubeY = 100
for z in range(0, 7):
	cubeX = 335 - (35*(z+1)) 
	cubeY += 60
	for i in range(0, z+1):
		cubeList[z][i] = Cube(cubeX, cubeY, cubeImg, blue_cubeImg, red_cubeImg)
		cubeX += 70

#5.0 Initialize sprites/obj.
myQbert = Qbert(3, 315, 130)

myDiscA = FlyingDisc(120, 360, 1) #disc A
myDiscB = FlyingDisc(500, 360, 2) #disc B

mySnake = Snake() #It will born as a ball when Qbert reach 3rd row.

redBall1 = Ball(redBall, 285, -70, 285, 210, 1) #Red Ball 1
redBall2 = Ball(redBall, 355, -70, 355, 210, 1) #Red Ball 2

greenBall1 = Ball(greenBall, 320, -70, 320, 280, 2) #Green Ball 1

Sam1 = Sam(250, -70, 250, 280) #Sam 1
Sam2 = Sam(390, -70, 390, 280) #Sam 2

myUggLeft = Ugg(uggLeft, -25, 500, 115, 500, 1, uggLeft_frozen) #Ugg 1
myUggRight = Ugg(uggRight, 875, 500, 525, 500, 2, uggRight_frozen) #Ugg 2

myLevel = Level(blue_cubeImg, red_cubeImg, cubeImg)

#6.0 /////////////////----------------------------------Main Game's Loop.-------------------------------------////////
while 1:
	screen.fill(BLACK) # fill screen with black
	
	#6.0.0 RESET! -- I'm going to reset everything when qbert dies or the user wins a round/level.
	if RESET == True:
		myQbert = Qbert(myQbert.lives, 315, 130) #QBERT RESET
		myDiscA = FlyingDisc(120, 360, 1) #disc A RESET
		myDiscB = FlyingDisc(500, 360, 2) #disc B RESET
		mySnake = Snake() #SNAKE RESET
		Sam1 = Sam(250, -70, 250, 280) #Sam 1 RESET
		Sam2 = Sam(390, -70, 390, 280) #Sam 2 RESET
		myUggLeft = Ugg(uggLeft, -25, 500, 115, 500, 1, uggLeft_frozen) #Ugg 1 RESET
		myUggRight = Ugg(uggRight, 875, 500, 525, 500, 2, uggRight_frozen) #Ugg 2 RESET
		greenBall1 = Ball(greenBall, 320, -70, 320, 280, 2) #Green Ball 1 RESET
		redBall1 = Ball(redBall, 285, -70, 285, 210, 1) #Red Ball 1 RESET
		redBall2 = Ball(redBall, 355, -70, 355, 210, 1) #Red Ball 2 RESET
		resetCubes(cubeList) #CUBES RESET
		cubeList[0][0].isBusy = 1
		RESET = False
	
	#6.0.1 Drawing lives on the screen.
	myQbert.drawLives(screen)
	
	#6.1 Drawing text and level.
	myLevel.drawLevel(screen)
	win = myLevel.winRound(cubeList) #Win function()! win == 1 if all cubes are the same color.
	
	#6.2.1 WINNING GAME? LET'S CHECK! -- It will start a lot of methods to reset all the GUI!
	if win == True: #Show win screen and RESET EVERYTHING!
		win = myLevel.winAnimation(screen)
		RESET = True #reset time
		
	#6.2.2 QBERT'S DEAD --- This "while" will be executed when qbert is dying. This is Qbert's isDead()
	if myQbert.y > 600: #OR COLLIDE WITH AN ENEMY!
		dead = True
		myQbert.lives -= 1
		if myQbert.lives < 0: #GAME OVER()
			myLevel.gameOver(screen)
		if dead == True: #Show lose screen and RESET EVERYTHING!
			dead = myQbert.isDead(screen)
			RESET = True #reset time..

	#6.3 Drawing cubes.
	for myList in cubeList:
		for elem in myList:
			elem.draw(screen)
			
	#6.3.5 ------------- Draw discs and flying Animation ----------------
	if pygame.time.get_ticks() % 500 < 300: #0.5 seconds
		myDiscA.animation = 1 if myDiscA.animation == 0 else 0
		myDiscB.animation = 1 if myDiscB.animation == 0 else 0
	
	if myQbert.x == 120 and myQbert.y == 330: #qbert jump on left disc.
		myQbert.nextX = 315
		myQbert.nextY = 130
		myDiscA.nextX = 315
		myDiscA.nextY = 160
	elif myQbert.x == 500 and myQbert.y == 330: #qbert jump on right disc.
		myQbert.nextX = 315
		myQbert.nextY = 130
		myDiscB.nextX = 315
		myDiscB.nextY = 160
	
	if myDiscA.y != myDiscA.nextY or myDiscA.x != myDiscA.nextX: #flying animation for left disc.
		myDiscA.flyingAnimation()
	elif myDiscB.y != myDiscB.nextY or myDiscB.x != myDiscB.nextX: #flying animation for right disc.
		myDiscB.flyingAnimation()
	elif myDiscA.x == 315 and myDiscA.y == 160: #Disc arrived to destination and now must be destroyed.
		myDiscA.x, myDiscA.y = 0, 0 #I need to change x and y or this statements will be repeated every single frame and my game crash.
		myDiscA.nextX, myDiscA.nextY = 0, 0 #This 2 assignment are very important!! discs are hidden, but if they stay in qbert position the game will be bugged.
		myDiscA.activated = 1
		cubeList[0][0].isBusy = 1
		mySnake = Snake() #SNAKE RESET
		myLevel.score += 500 # +500 SCORE! KILL THE SNAKE BOUNTY!
		
	elif myDiscB.x == 315 and myDiscB.y == 160: #Disc arrived to destination and now must be destroyed.
		myDiscB.x, myDiscB.y = 0, 0 #I need to change x and y or this statemetns will be repeated every single frame and my game crash.
		myDiscB.nextX, myDiscB.nextY = 0, 0 #This 2 assignment are very important!! discs are hidden, but if they stay in qbert position the game will be bugged.
		myDiscB.activated = 1
		cubeList[0][0].isBusy = 1
		mySnake = Snake() #SNAKE RESET
		myLevel.score += 500 # +500 SCORE! KILL THE SNAKE BOUNTY!

	myDiscA.draw(screen)
	myDiscB.draw(screen)
	
	#6.4 QBERT MOVING EVENT ---- Checking for an event key_pressed ----
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN and myQbert.nextMOVE == True:
			if pygame.key.get_pressed()[pygame.K_UP]: #UP key pressed
				indX, indY = findSprite(cubeList, 1)
				myQbert.imageToBlit = myQbert.image #Qbert is looking LEFT now!
				if indX == 4 and indY == 0 and myDiscA.activated == 0: #This means that qbert is in the left cube to jump on the disc and the disc is not activated yet!
					myQbert.jumpOnDisc(1)
				elif indX-1 < 0 or indY-1 < 0: #This means that qBert jump down from a cube.
					myQbert.nextX, myQbert.nextY = myQbert.x - 50, myQbert.y + 500
					myQbert.speed = 25
				else: #This will be executed when Q*bert will move without dying or using disc.
					newX, newY = indX-1, indY-1
					myQbert.endAnimation = True
					myQbert.nextX, myQbert.nextY = cubeList[indX-1][indY-1].x+15, cubeList[indX-1][indY-1].y-30 #+15 and -30 because qbert must be drawn not inside the cube but above che cube!
					
			elif pygame.key.get_pressed()[pygame.K_DOWN]: #DOWN key pressed
				indX, indY = findSprite(cubeList, 1)
				myQbert.imageToBlit = myQbert.imageInverse #Q*bert is looking RIGHT now!
				if indX+1 < 7: #This means that Q*bert is moving in another cube.
					newX, newY = indX+1, indY+1
					myQbert.endAnimation = True
					myQbert.nextX, myQbert.nextY = cubeList[indX+1][indY+1].x+15, cubeList[indX+1][indY+1].y-30 #+15 and -30 because qbert must be drawn not inside the cube but above che cube!
				else: #This means that qBert jump down from a cube.
					myQbert.nextX, myQbert.nextY = myQbert.x, myQbert.y + 150
					myQbert.speed = 25
					
			elif pygame.key.get_pressed()[pygame.K_RIGHT]: #RIGHT key pressed
				indX, indY = findSprite(cubeList, 1)
				myQbert.imageToBlit = myQbert.imageInverse #Qbert is looking RIGHT now!
				if indX-1 >= 0 and len(cubeList[indX-1]) > indY:  #I have to check if the previous row doesn't make me "out of range" for indY.
					newX, newY = indX-1, indY
					myQbert.endAnimation = True
					myQbert.nextX, myQbert.nextY = cubeList[indX-1][indY].x+15, cubeList[indX-1][indY].y-30 #+15 and -30 because qbert must be drawn not inside the cube but above che cube!
				elif indX == 4 and indY == 4 and myDiscB.activated == 0: #This means that qbert is in the right cube to jump on the disc and the disc is not activated yet!
					myQbert.jumpOnDisc(2)
				else: #This means that qBert jump down from a cube.
					myQbert.nextX, myQbert.nextY = myQbert.x + 50, myQbert.y + 500
					myQbert.speed = 25
					
			elif pygame.key.get_pressed()[pygame.K_LEFT]: #LEFT key pressed
				indX, indY = findSprite(cubeList, 1)
				myQbert.imageToBlit = myQbert.image #Qbert is looking LEFT now!
				if indX+1 < 7:
					newX, newY = indX+1, indY
					myQbert.endAnimation = True
					myQbert.nextX, myQbert.nextY = cubeList[indX+1][indY].x+15, cubeList[indX+1][indY].y-30 #+15 and -30 because qbert must be drawn not inside the cube but above che cube!
				else: #This means that qBert jump down from a cube.
					myQbert.nextX, myQbert.nextY = myQbert.x, myQbert.y + 150
					myQbert.speed = 25
			
	#6.5 Qbert moving animation. It will move when he finds that actual position is different from nextX or nextY.
	myQbert.animation()
		
	if myQbert.endAnimation == True and myQbert.nextMOVE == True: #This is important because let me draw and update cubes AFTER the end of the animation. Useful to create a more efficient game.
		myLevel.score = cubeList[newX][newY].increaseIsActiveIfPossible(myLevel.levels, myLevel.score)  #Decide if a cube must be colored or not, increase score!
		cubeList[newX][newY].isBusy = 1
		myQbert.endAnimation = False
		
	#6.6 Draw myQbert
	myQbert.draw(screen) 
	
	#6.7 ------------- Draw Snake.. -------------------
	for cont in range(0,3):
		if cubeList[2][cont].isBusy == 1:
			mySnake.ItsTimeToSpawn = True
			
	if mySnake.isBall == 0 and mySnake.ItsTimeToSpawn == True: #It becomes "1" for the first time...and snake will born.
		mySnake.snakeBorn()
		cubeList[0][0].isBusy = 2

	if mySnake.isBall == 1: #Snake is born..
		if mySnake.snakeNextMOVE == True:
			snakeIndexX, snakeIndexY = findSprite(cubeList, 2)
			mySnake.snakeNextMOVE = False
		snakeIndexX, snakeIndexY = mySnake.followBert(snakeIndexX, snakeIndexY, cubeList, myQbert.x, myQbert.y)
		
		if freeze == 0: 
			mySnake.animate()
		
		if mySnake.x == mySnake.nextX and mySnake.y == mySnake.nextY: #I need to put "2" inside my cube AT THE END OF THE ANIMATION. 
			if cubeList[snakeIndexX][snakeIndexY].isBusy == 1: #COLLISION WITH QBERT!!
				myQbert.nextX, myQbert.nextY = myQbert.x, myQbert.y + 700 #Q*bert is dead!
				myQbert.speed = 25
				myQbert.nextMOVE = False # If I don't put this to False my game will crash if I do an event keydown while he is dying.
			else:
				cubeList[snakeIndexX][snakeIndexY].isBusy = 2
				mySnake.snakeNextMOVE = True

	mySnake.draw(screen, freeze)
	
	#6.8.1 ------------- Draw red balls.. --------------------------
	if redBall1.timer + 7000 < pygame.time.get_ticks() and redBall1.isBorn == 0 and cubeList[1][0].isBusy == 0: #every 7 seconds
		redBall1.Born(cubeList[1][0], 4)
		
	if redBall1.timer + 14000 < pygame.time.get_ticks() and redBall2.isBorn == 0 and cubeList[1][1].isBusy == 0: #every 14 seconds
		redBall2.Born(cubeList[1][1], 41)
			
	if redBall1.isBorn == 1:
		if redBall1.nextMOVE == 1:
			ballIndexX, ballIndexY = findSprite(cubeList, 4)
			redBall1.nextMOVE = 0
		ballIndexX, ballIndexY = redBall1.RandomPath(ballIndexX, ballIndexY, cubeList)
		
		if freeze == 0: 
			redBall1.animation(myLevel.levels) #Animation will go faster if I'm on level 3.
			
		if redBall1.x == redBall1.nextX and redBall1.y == redBall1.nextY and redBall1.y < 650: #I need to put the "4" inside my cube AT THE END OF THE ANIMATION.
			if cubeList[ballIndexX][ballIndexY].isBusy == 1: #THERE IS QBERT! COLLISION!!
				myQbert.nextX, myQbert.nextY = myQbert.x, myQbert.y + 700 #Q*bert is dead!
				myQbert.speed = 25
				myQbert.nextMOVE = False # If I don't put this to False my game will crash if I do an event keydown while he is dying.
			else:
				cubeList[ballIndexX][ballIndexY].isBusy = 4
		elif redBall1.x == redBall1.nextX and redBall1.y == redBall1.nextY and redBall1.y > 650: #My ball fall down and I reset her.
			print("Red ball 1 dead")
			redBall1 = Ball(redBall, 285, -70, 285, 210, 1)
	
	
	if redBall2.isBorn == 1:
		if redBall2.nextMOVE == 1:
			ballIndexX2, ballIndexY2 = findSprite(cubeList, 41)
			redBall2.nextMOVE = 0
		ballIndexX2, ballIndexY2 = redBall2.RandomPath(ballIndexX2, ballIndexY2, cubeList)
		
		if freeze == 0: 
			redBall2.animation(myLevel.levels) #Animation will go faster if I'm on level 3.
		
		if redBall2.x == redBall2.nextX and redBall2.y == redBall2.nextY and redBall2.y < 650: #I need to put the "41" inside my cube AT THE END OF THE ANIMATION.
			if cubeList[ballIndexX2][ballIndexY2].isBusy == 1: #THERE IS QBERT! COLLISION!!
				myQbert.nextX, myQbert.nextY = myQbert.x, myQbert.y + 700 #Q*bert is dead!
				myQbert.speed = 25
				myQbert.nextMOVE = False # If I don't put this to False my game will crash if I do an event keydown while Q*bert is dying.
			else:
				cubeList[ballIndexX2][ballIndexY2].isBusy = 41
		elif redBall2.x == redBall2.nextX and redBall2.y == redBall2.nextY and redBall2.y > 650: #My ball fall down and I reset her.
			print("Red ball 2 dead")
			redBall2 = Ball(redBall, 355, -70, 355, 210, 1)

	redBall1.draw(screen, freeze)
	redBall2.draw(screen, freeze)
	
	#6.8.2 ------------- Draw 2xSam! (Green enemies)..
	if myLevel.levels == 3 and Sam1.timer + 10000 < pygame.time.get_ticks() and Sam1.Born == 0 and cubeList[2][0].isBusy == 0: #every 10 seconds
		Sam1.samBorn(cubeList[2][0], 6)
		
	if myLevel.levels == 3 and Sam2.timer + 12000 < pygame.time.get_ticks() and Sam2.Born == 0 and cubeList[2][2].isBusy == 0: #every 12 seconds
		Sam2.samBorn(cubeList[2][2], 61)
	
	if Sam1.Born == 1:
		if Sam1.nextMOVE == 1:
			SamIndexX, SamIndexY = findSprite(cubeList, 6)
			Sam1.nextMOVE = 0
		SamIndexX, SamIndexY = Sam1.samRandomPath(SamIndexX, SamIndexY, cubeList)
		
		if freeze == 0: 
			Sam1.animate()
			
		if Sam1.x == Sam1.nextX and Sam1.y == Sam1.nextY:
			if cubeList[SamIndexX][SamIndexY].isBusy == 1: #There is qbert! COLLISION! +300 SCORE!
				myLevel.score += 300 # +300 SCORE!
				Sam1 = Sam(250, -70, 250, 280)
			else:
				cubeList[SamIndexX][SamIndexY].isBusy = 6
				if cubeList[SamIndexX][SamIndexY].isActive == 2 or cubeList[SamIndexX][SamIndexY].isActive == 1: #clean a color! damn Sam
					cubeList[SamIndexX][SamIndexY].isActive -= 1
			Sam1.nextMOVE = 1

	if Sam2.Born == 1:
		if Sam2.nextMOVE == 1:
			SamIndexX2, SamIndexY2 = findSprite(cubeList, 61)
			Sam2.nextMOVE = 0
		SamIndexX2, SamIndexY2 = Sam2.samRandomPath(SamIndexX2, SamIndexY2, cubeList)
		
		if freeze == 0: 
			Sam2.animate()
			
		if Sam2.x == Sam2.nextX and Sam2.y == Sam2.nextY:
			if cubeList[SamIndexX2][SamIndexY2].isBusy == 1: #There is qbert! COLLISION! +300 SCORE!
				myLevel.score += 300 # +300 SCORE!
				Sam2 = Sam(390, -70, 390, 280)
			else:
				cubeList[SamIndexX2][SamIndexY2].isBusy = 61
				if cubeList[SamIndexX2][SamIndexY2].isActive == 2 or cubeList[SamIndexX2][SamIndexY2].isActive == 1: #Clean a color! Damn Sam :)
					cubeList[SamIndexX2][SamIndexY2].isActive -= 1
			Sam2.nextMOVE = 1
	
	Sam1.draw(screen, freeze)
	Sam2.draw(screen, freeze)
	
	#6.8.3 ------------- Draw 2xUGG! (Purple enemies).. ------------------------
	if myUggLeft.timer + 9000 < pygame.time.get_ticks() and myUggLeft.Born == 0 and cubeList[6][0].isBusy == 0: #every 9 seconds
		myUggLeft.uggBorn(cubeList[6][0], 3)
		
	if myUggRight.timer + 15000 < pygame.time.get_ticks() and myUggRight.Born == 0 and cubeList[6][6].isBusy == 0: #every 15 seconds
		myUggRight.uggBorn(cubeList[6][6], 31)
	
	if myUggLeft.Born == 1:
		if myUggLeft.nextMOVE == 1:
			uggIndexX, uggIndexY = findSprite(cubeList, 3)
			myUggLeft.nextMOVE = 0
		uggIndexX, uggIndexY = myUggLeft.randomPath(uggIndexX, uggIndexY, cubeList)
		
		if freeze == 0: 
			myUggLeft.animate()
			
		if myUggLeft.x == myUggLeft.nextX and myUggLeft.y == myUggLeft.nextY and myUggLeft.isFalling == 0: #If he is not fell down, I write the "3" only at the END of the animation.
			if cubeList[uggIndexX][uggIndexY].isBusy == 1: #THERE IS QBERT! COLLISION!!
				myQbert.nextX, myQbert.nextY = myQbert.x, myQbert.y + 700 #Q*bert is dead!
				myQbert.speed = 25
				myQbert.nextMOVE = False # If I don't put this to False my game will crash if I do an event keydown while Q*bert is dying.
			elif cubeList[uggIndexX][uggIndexY].isBusy != 1:
				cubeList[uggIndexX][uggIndexY].isBusy = 3
				#for q in range(0, 7): #print me the situation
					#lista_temporanea = []
					#for e in range(0, q+1):
						#lista_temporanea.append(cubeList[q][e].isBusy)
					#print(lista_temporanea)
					#if q == 6:
						#print("")
		elif myUggLeft.x == myUggLeft.nextX and myUggLeft.y == myUggLeft.nextY and myUggLeft.isFalling == 1 and myUggLeft.x > 650: #If he felt down.
			print("Ugg Left dead")
			myUggLeft = Ugg(uggLeft, -25, 560, 80, 560, 1, uggLeft_frozen) #Ugg 1

	if myUggRight.Born == 1:
		if myUggRight.nextMOVE == 1:
			uggIndexX2, uggIndexY2 = findSprite(cubeList, 31)
			myUggRight.nextMOVE = 0
		uggIndexX2, uggIndexY2 = myUggRight.randomPath(uggIndexX2, uggIndexY2, cubeList)
		
		if freeze == 0: 
			myUggRight.animate()
			
		if myUggRight.x == myUggRight.nextX and myUggRight.y == myUggRight.nextY and myUggLeft.isFalling == 0: #If he isn't fell down, I write the "31" ONLY at the END of the animation.
			if cubeList[uggIndexX2][uggIndexY2].isBusy == 1: #THERE IS QBERT! COLLISION!!
				myQbert.nextX, myQbert.nextY = myQbert.x, myQbert.y + 700 #Q*bert is dead!
				myQbert.speed = 25
				myQbert.nextMOVE = False #If I don't put this to False my game will crash if I do an event keydown while Q*bert is dying.
			elif cubeList[uggIndexX2][uggIndexY2].isBusy != 1:
				cubeList[uggIndexX2][uggIndexY2].isBusy = 31
				#for q in range(0, 7): #print me the situation
					#lista_temporanea = []
					#for e in range(0, q+1):
						#lista_temporanea.append(cubeList[q][e].isBusy)
					#print(lista_temporanea)
					#if q == 6:
						#print("")
		elif myUggRight.x == myUggRight.nextX and myUggRight.y == myUggRight.nextY and myUggLeft.isFalling == 1 and myUggRight.x < 0: #if he felt down.
			print("Ugg Right dead")
			myUggRight = Ugg(uggRight, 910, 560, 560, 560, 2, uggRight_frozen) #Ugg 2
			
	myUggLeft.draw(screen, freeze)
	myUggRight.draw(screen, freeze)
	
	#6.8.4 ------------- Draw Green Ball! -----------------
	if greenBall1.timer + 15000 < pygame.time.get_ticks(): #every 15 seconds
		if greenBall1.isBorn == 0 and cubeList[2][1].isBusy == 0:
			greenBall1.Born(cubeList[2][1], 5)
			
	if greenBall1.isBorn == 1:
		if greenBall1.nextMOVE == 1:
			greenBallIndexX, greenBallIndexY = findSprite(cubeList, 5)
			greenBall1.nextMOVE = 0
		greenBallIndexX, greenBallIndexY = greenBall1.RandomPath(greenBallIndexX, greenBallIndexY, cubeList)
		greenBall1.animation(myLevel.levels) #Animation will go faster if I'm on level 3.
		if greenBall1.x == greenBall1.nextX and greenBall1.y == greenBall1.nextY and greenBall1.y < 650: #Means ball is not fall down yet.
			if cubeList[greenBallIndexX][greenBallIndexY].isBusy == 1: #There is qbert! COLLISION! +100 SCORE!
				freeze = 1 #It's time to freeze everyone!
				timerFreezing = pygame.time.get_ticks() #I need to save the actual time, and then after 3000 milliseconds I can stop the freezing.
				myLevel.score += 100 # +100 SCORE!
				greenBall1 = Ball(greenBall, 320, -70, 320, 280, 2) #Green Ball 1
				greenBall1.timer = pygame.time.get_ticks() #this time + 15 secs and a new green ball will be spawned!
			else: #if there isn't qbert..
				cubeList[greenBallIndexX][greenBallIndexY].isBusy = 5
		elif greenBall1.x == greenBall1.nextX and greenBall1.y == greenBall1.nextY and greenBall1.y > 650: #Ball fall down.
			print("Green Ball Dead")
			greenBall1 = Ball(greenBall, 320, -70, 320, 280, 2) #Green Ball 1
			greenBall1.timer = pygame.time.get_ticks() #this time + 15 secs and a new green ball will be spawned!

	greenBall1.draw(screen, freeze)
		
	#6.X NEW LIFE -- if score > 8000 get a new life.
	if myLevel.extraLife == False and myLevel.score > 8000:
		myLevel.extraLife = True
		myQbert.lives += 1
	
	#6.X START GAME -- This "while" will be executed just one time, when the user click left or right key for the first time, for starting the game.
	while start == True:
		start = myLevel.startingPoint(screen)
		if start == False: #if I click ENTER key..
			cubeList[0][0].isBusy = 1
	
	#6.X FREEZE -- If freeze == 1 then after 3 seconds it comes back to 0.
	if freeze == 1 and timerFreezing + 3000 < pygame.time.get_ticks():
		freeze = 0
	
	for _ in pygame.event.get():
		if _.type == QUIT:
			pygame.quit()
			sys.quit()
			
	pygame.display.update()
	pygame.time.Clock().tick(FPS)


