# https://www.freecodecamp.org/news/python-projects-for-beginners#rock-paper-scissors-python-project
# main batu gunting kerta dengan kopmputer

# -----first version

# import random as rnd

# 1 rock, 2 scissor, 3 paper

# isStop = False
# while isStop == False:
# 	comPicked = rnd.randint(1, 3)
# 	userIn = input("what you pick? r rock, s scissor, p paper -> ")

# 	if userIn.lower() == "r" and comPicked == 1:
# 		print("Its draw")
# 	elif userIn.lower() == "r" and comPicked == 2:
# 		print("You win!!")
# 		isStop = True
# 	elif userIn.lower() == "r" and comPicked == 3:
# 		print("You lose!!")

# 	if userIn.lower() == "s" and comPicked == 1:
# 		print("You lose!!")
# 	elif userIn.lower() == "s" and comPicked == 2:
# 		print("Its draw")
# 	elif userIn.lower() == "s" and comPicked == 3:
# 		print("You win!!")
# 		isStop = True

# 	if userIn.lower() == "p" and comPicked == 1:
# 		print("You win!!")
# 		isStop = True
# 	elif userIn.lower() == "p" and comPicked == 2:
# 		print("You lose!!")
# 	elif userIn.lower() == "p" and comPicked == 3:
# 		print("Its draw")

# ---- second version
# import random as rnd

# class RockScissorPaper():
# 	loseText = "You lose!!"
# 	winText = "You win!!"
# 	drawText = "Its draw."

# 	def __init__(self):
# 		self.comPicked = 0
# 		self.isStop = False
# 		self.userIn = ""

# 	def GenerateComPicked(self):
# 		# 1 rock, 2 scissor, 3 paper
# 		self.comPicked = rnd.randint(1, 3)

# 	def RockResult(self):
# 		if self.comPicked == 1:
# 			print(self.drawText)
# 		elif self.comPicked == 2:
# 			print(self.winText)
# 			self.isStop = True
# 		elif self.comPicked == 3:
# 			print(self.loseText)

# 	def ScissorResult(self):
# 		if self.comPicked == 1:
# 			print(self.loseText)
# 		elif self.comPicked == 2:
# 			print(self.drawText)
# 		elif self.comPicked == 3:
# 			print(self.winText)
# 			self.isStop = True

# 	def PaperResult(self):
# 		if self.comPicked == 1:
# 			print(self.winText)
# 			self.isStop = True
# 		elif self.comPicked == 2:
# 			print(self.loseText)
# 		elif self.comPicked == 3:
# 			print(self.drawText)

# 	def ProcessResult(self):
# 		if self.userIn.lower() == "r":
# 			self.RockResult()
# 		elif self.userIn.lower() == "s":
# 			self.ScissorResult()
# 		elif self.userIn.lower() == "p":
# 			self.PaperResult()

# 	def Main(self):
# 		while self.isStop == False:
# 			self.GenerateComPicked()

# 			self.userIn = input("what you pick? r rock, s scissor, p paper -> ")

# 			self.ProcessResult()

# tes1 = RockScissorPaper()
# tes1.Main()


# -------- third version


import random as rnd

class RockScissorPaper():
	loseText = "You lose!!"
	winText = "You win!!"
	drawText = "Its draw."

	def __init__(self):
		self.comPicked = 0
		self.isStop = False
		self.userIn = ""

	def GenerateComChoices(self):
		self.comPicked = rnd.choice(["r", "s", "p"])

	def ProcessResult(self):
		if self.userIn == self.comPicked:
			print(self.drawText)
		elif (self.userIn == "r" and self.comPicked == "p") or \
			(self.userIn == "p" and self.comPicked == "r") or \
			(self.userIn == "s" and self.comPicked == "p"):
			print(self.winText)
			self.isStop = True
		else:
			print(self.loseText)

	def Main(self):
		while self.isStop == False:
			self.GenerateComChoices()

			self.userIn = str(input("what you pick? r rock, s scissor, p paper -> ")).lower()

			self.ProcessResult()

tes1 = RockScissorPaper()
tes1.Main()