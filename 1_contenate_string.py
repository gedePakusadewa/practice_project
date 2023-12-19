
# https://www.freecodecamp.org/news/python-projects-for-beginners/#mad-libs-python-project
# menerima beberapa input user kemudian menampilkan gabungan text itu dalam console

# ----first version
# def Concatenate(str1, str2):
# 	return str1 + str2

# str1 = input("first word-> ")
# str2 = input("second word-> ")

# print(Concatenate(str1, str2))

# -----second version
def Concatenate(listStr):
	temp = ""
	for str1 in listStr:
		temp += str1 + " "

	return temp

isStop = False
listStr = []
while isStop == False:
	print("type STOP to close")
	print()
	str1 = input("type word ->")
	if str1.upper() != "STOP":
		listStr.append(str1)
	elif str1.upper() == "STOP":
		isStop = True

	print("--> " + Concatenate(listStr))
