# https://www.freecodecamp.org/news/python-projects-for-beginners/#guess-the-number-game-python-project-computer-
# komputer menebak angka 3 digit dari user

#--- first version

# import random as rdm

# isStop = False
# userNumber = 10
# while isStop == False:
# 	if userNumber == 10:
# 		userNumber = int(input("Masukkan angka kurang dari 10 dan lebih besar dari -1 -> "))
# 	elif userNumber != 10:
# 		print(f"---your number {userNumber}----")
# 		computerNum = rdm.randint(1, 9)

# 		userInput = input(f"is {computerNum} is too high (type h), too low (type l), or correct (type c)--> ")

# 		if userInput.lower() == "h":
# 			computerNum = rdm.randint(1, computerNum)
# 		elif userInput.lower() == "l":
# 			computerNum = rdm.randint(computerNum, 9)
# 		elif userInput.lower() == "c":
# 			print(f"Your number is {computerNum}")
# 			isStop = True

# ---- second version
import random as rdm

isStop = False
userNum = 100
upLimit = 100
botLimit= -1
while isStop == False:
	if userNum == 100:
		userNum = int(input("Masukkan angka kurang dari 101 dan lebih besar dari -1 -> "))
	elif userNum != 100:
		print(f"---your number {userNum}----")
		comNum = rdm.randint(botLimit, upLimit)

		userInput = input(f"is {comNum} is too high (type h), too low (type l), or correct (type c)--> ")

		if userInput.lower() == "h":
			upLimit = comNum
			comNum = rdm.randint(botLimit, upLimit)
		elif userInput.lower() == "l":
			botLimit = comNum
			comNum = rdm.randint(botLimit, upLimit)
		elif userInput.lower() == "c":
			print(f"Your number is {comNum}")
			isStop = True