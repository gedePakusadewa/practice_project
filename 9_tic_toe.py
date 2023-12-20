# https://www.freecodecamp.org/news/python-projects-for-beginners#tic-tac-toe-python-project
# visualisation task https://www.youtube.com/watch?v=8ext9G7xspg&t=2153s

# make two method to display what position player want and mwthod to calculate user input/move
import math as mt

displayLine = ""
filledPosition = []

def display(position, player):

	if player != "start":
		filledPosition.append(position)

	line = ""

	dataPosition = {
		"1":"2",
		"2":"4",
		"3":"6",
		"4":"9",
		"5":"11",
		"6":"13",
		"7":"16",
		"8":"18",
		"9":"20"
	}

	i = 1
	for x in range(1, 22, +1):

		if i % 2 == 0:

			if int(dataPosition[position]) == x and (player != "start"):

				if player == "cpu":
					line += "X"
				else:
					line += "O"
			else:
				line += "-"
		else:
			line += "|"

		if x % 7 == 0:
			line += "\n"
			i = 0

		i += 1

	return line

displayLine = display("8", "cpu")

def get_unfilled_position():
	for x in range(1, 10, +1):
		if x not in filledPosition:
			return x
	return 0

def cpu_calculate(position):

	if position == 1:
		if 2 not in filledPosition:
			display(2, "cpu")
		elif 5 not in filledPosition:
			display(5, "cpu")
		elif 4 not in filledPosition:
			display(4, "cpu")
		elif get_unfilled_position() == 0:
			print("Its tie")
		else:
			display(get_unfilled_position(), "cpu")

isStop = False
while isStop == False:
	display(1, "start")
	ins = input("Your Move -> ")

	if int(ins) == ins:
		cpu_calculate(ins)
	else:
		isStop = True

# rulesSet = {
# 	"1" : {
# 		"2" : "2",
# 		"5" : "5",
# 		"4" : "4"
# 	}
# }


#|O|X|O|
#|O|X|O|
#|O|X|O|	
# |-|-|-|
# -|-|-|-
# |-|-|-|
#|1|2|3|
#|4|5|6|
#|7|8|9|	

# jika 1 = 0 maka 
# 	jika 2 kosong maka 2 X
# 	jika 5 kosong maka 5 X
# 	jika 4 kosong maka 4 X
# 	jika tiga itu tidak ada yg kosong maka cari tempat lain yang kosong maka X
# 	jika tidak ada tempat kosong maka "tie"