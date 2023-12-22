class Cube():
	def __init__(self, newX, newY, cube, blue_cubeImg, red_cubeImg):
		self.isActive = 0 #Number of times Q*bert need to jump on a cube to win.
		self.x = newX
		self.y = newY
		
		self.cube = cube
		self.blueCube = blue_cubeImg
		self.RedCube = red_cubeImg
		
		self.isBusy = 0 #Read istructions below.
		
	def draw(self, screen): #Draw in the screen.
		if self.isActive == 0:
			screen.blit(self.cube,(self.x, self.y))
		elif self.isActive == 1:
			screen.blit(self.blueCube,(self.x, self.y))
		elif self.isActive == 2:
			screen.blit(self.RedCube,(self.x, self.y))
			
	def increaseIsActiveIfPossible(self, level, score):
		if level == 1 and self.isActive == 0:
			self.isActive += 1
			score += 25 #Score point +25 for moving on the cubes!
			return score
		elif level > 1 and self.isActive < 2:
			self.isActive += 1
			score += 25 #Score point +25 for moving on the cubes!
			return score
		return score

#-------RULES OF isBusy ATTRIBUTE---------------#
#isBusy == 0 if Empty
#isBusy == 1 if Qbert 
#isBusy == 2 if Snake 
#isBusy == 3 and 31 if 2xUgg
#isBusy == 4 and 41 if 2xRedball
#isBusy == 5 if Greenball
#isBusy == 6 and 61 if 2xSam

#-------ALL X AND Y VALUES OF MY CUBES IN THE GAME---------------#
#screen.blit(cubeImg,(300,160)) #0-0

#screen.blit(cubeImg,(265,220)) #1-0
#screen.blit(cubeImg,(335,220)) #1-1

#screen.blit(cubeImg,(230,280)) #2-0
#screen.blit(cubeImg,(300,280)) #2-1
#screen.blit(cubeImg,(370,280)) #2-2

#screen.blit(cubeImg,(195,340)) #3-0
#screen.blit(cubeImg,(265,340)) #3-1
#screen.blit(cubeImg,(335,340)) #3-2
#screen.blit(cubeImg,(405,340)) #3-3

#screen.blit(cubeImg,(160,400)) #4-0
#screen.blit(cubeImg,(230,400)) #4-1
#screen.blit(cubeImg,(300,400)) #4-2
#screen.blit(cubeImg,(370,400)) #4-3
#screen.blit(cubeImg,(440,400)) #4-4

#screen.blit(cubeImg,(125,460)) #5-0
#screen.blit(cubeImg,(195,460)) #5-1
#screen.blit(cubeImg,(265,460)) #5-2
#screen.blit(cubeImg,(335,460)) #5-3
#screen.blit(cubeImg,(405,460)) #5-4
#screen.blit(cubeImg,(475,460)) #5-5

#screen.blit(cubeImg,(90,520)) #6-0
#screen.blit(cubeImg,(160,520)) #6-1
#screen.blit(cubeImg,(230,520)) #6-2
#screen.blit(cubeImg,(300,520)) #6-3
#screen.blit(cubeImg,(370,520)) #6-4
#screen.blit(cubeImg,(440,520)) #6-5
#screen.blit(cubeImg,(510,520)) #6-6
