# https://www.freecodecamp.org/news/python-projects-for-beginners#hangman-python-project
# membuat game hangman


# --- first version
# import random as rnd

# wordData = [
# 	"academic", "accident", "band", "bathroom", "boyfriend",
# 	"cat", "character", "coffee", "decade", "discussion",
# 	"entertainment", "expectation", "gallery", "guideline", "husband",
# 	"independent", "junior", "library", "office", "perfect"
# 	]

# rndWord = rnd.choice(wordData)

# def PrintBlankWord(word):
# 	output = ""
# 	for item  in word:
# 		output += "_"

# 	return output

# def PrintFilledWord(char, word, oldWord):
# 	output = list(oldWord)
# 	for item  in range(len(word)):
# 		if  word[item] == char :
# 			output[item] = char

# 	return "".join(output)

# def CheckInputUser(inputUser, word, oldWord):
# 	output  = oldWord
# 	if inputUser in word:
# 		output = PrintFilledWord(inputUser, word, oldWord)

# 	return output

# def IsAllFill(word):
# 	status = True
# 	for item in word:
# 		if item == "_" :
# 			status = False

# 	return status

# isStop = False
# tempWord = PrintBlankWord(rndWord.upper())
# tempInput = []
# totalChange = len(tempWord) + 3
# while isStop == False:
# 	# print(rndWord)
# 	print(tempWord)
# 	if tempInput:
# 		print(f"This is all your used word: {' '.join(tempInput)}")

# 	inputUser = input("Masukkan huruf -> ")
# 	tempInput.append(inputUser.upper())

# 	if tempWord == CheckInputUser(inputUser, rndWord, tempWord):
# 		print(f"Your '{inputUser.upper()}' is not in word")
# 	else:
# 		tempWord = CheckInputUser(inputUser, rndWord, tempWord)

# 	if IsAllFill(tempWord):
# 		isStop = True
# 		print(f"Congratulation your guess word {tempWord}")

# 	totalChange -= 1
# 	if totalChange == 0:
# 		print(f"You run out of step, you lose, the correct word is {rndWord.upper()}")
# 		isStop = True
# 	else:		
# 		print(f"{totalChange} step is left")


# ----- second version
import random as rnd

class Hangman():
	wordsData = [
		"academic", "accident", "band", "bathroom", "boyfriend",
		"cat", "character", "coffee", "decade", "discussion",
		"entertainment", "expectation", "gallery", "guideline", "husband",
		"independent", "junior", "library", "office", "perfect"
	]

	freeMove = 3

	def __init__(self):
		self.isStop = False
		self.randomWord = rnd.choice(self.wordsData).upper()
		self.blankWord = self.GenerateBlankWord()
		self.guessedWord = self.blankWord
		self.allUserInput = []
		self.totalStep = len(self.randomWord) + self.freeMove

	def GenerateBlankWord(self):
		output = ""
		for item in self.randomWord:
			output += "_"

		return output

	def GenerateFilledWord(self, inputUser):
		if not inputUser:
			return self.guessedWord

		output = list(self.guessedWord)
		for item in range(len(self.randomWord)):
			if self.randomWord[item] == inputUser:
				output[item] = inputUser

		return "".join(output)

	def IsAllFilled(self):
		for item in self.guessedWord:
			if item == "_" :
				return False

		return True

	def SetAllUserInput(self, char):
		self.allUserInput.append(char)

	def SetGuessedWord(self, word):
		self.guessedWord = word

	def SetIsStop(self, value):
		self.isStop = value

	def SetTotalStep(self, value):
		self.totalStep -= value

	def Main(self):
		tempWord = self.GenerateBlankWord()
		while self.isStop == False:
			print()
			print()
			print(tempWord)

			if self.allUserInput:
				print(f"This is all your used word: {' '.join(self.allUserInput)}")

			inputUser = input("Please type your character-> ")
			self.SetAllUserInput(inputUser.upper())

			tempWord = self.GenerateFilledWord(inputUser.upper())
			if tempWord == self.guessedWord:
				print(f"Your '{inputUser.upper()}' is not in word")
			else:
				self.SetGuessedWord(tempWord)

			if self.IsAllFilled():
				self.SetIsStop(True)
				print()
				print(f"Congratulation your guess word {tempWord}")

			self.SetTotalStep(1)
			if self.totalStep == 0:
				print()
				print(f"You run out of step, you lose, the correct word is {self.randomWord}")
				self.SetIsStop(True)
			else: 
				print(f"{self.totalStep} steps are left")

tes1 = Hangman()
tes1.Main()
