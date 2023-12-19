# https://www.freecodecamp.org/news/python-projects-for-beginners/#guess-the-number-game-python-project-user-
# user menebak angka yg di generate computer


# --- first version
# import random as rnd

# comNum = rnd.randint(-1, 9)

# isStop = False

# while isStop == False:
# 	 userIn = int(input("your number -> "))

# 	 if userIn == comNum:
# 	 	print(f"Your correct sir, {comNum}")
# 	 	isStop = True
# 	 elif userIn != comNum:
# 	 	print(f"Incorrect number {userIn}")

# --- second version

import random as rnd

class UserGuess():
	def __init__(self):
		self.num = rnd.randint(1, 100)
		self.isStop = False
		self.userIn = -1

	def PrintResponse(self):
		self.PrintCorrectIncorrect()
		self.PrintClue()

	def PrintCorrectIncorrect(self):
		if self.userIn == self.num:
			print(f"Your correct sir, {self.num}")
			self.isStop = True
		elif self.userIn != self.num:
			print(f"Incorrect number {self.userIn}")

	def PrintClue(self):
		if self.userIn < self.num:
			print(f"Higher then {self.userIn}")
		elif self.userIn > self.num:
			print(f"Lower then {self.userIn}")

	def Main(self):
		while self.isStop == False:
			self.userIn = int(input("your number -> "))

			self.PrintResponse()

tes1 = UserGuess()

tes1.Main()