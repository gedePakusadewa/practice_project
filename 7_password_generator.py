# https://www.freecodecamp.org/news/python-projects-for-beginners#password-generator-python-project
# generate password berdasarkan jumlah password dan panjang password

#--- first version
# import random as rnd

# data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# passSum = int(input("how many password -> "))
# passLen = int(input("password length -> "))

# def generate_password(length):
# 	if length <= 0:
# 		return ""

# 	result = ""
# 	for x in range(length):
# 		result = result + (rnd.choice(data))

# 	return result
# for _ in range(passSum):
# 	print(generate_password(passLen))

# ---- second version
import random as rnd

class GeneratePassword():
	data = [
		'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
		'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
		'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
		't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
		'#', '$', '%', '&', "'", '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
	]

	def __init__(self):
		self.passLen = 0

	def generate_password(self):
		result = ""
		for x in range(self.passLen):
			result += rnd.choice(self.data)

		return result

	def run(self):
		passSum = int(input("how many password -> "))
		self.passLen = int(input("password length -> "))

		if self.passLen <= 0:
			print("")
			return 

		while passSum:
			print(self.generate_password())
			passSum -= 1

tes1 = GeneratePassword()
tes1.run()

