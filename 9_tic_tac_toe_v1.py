# https://www.freecodecamp.org/news/python-projects-for-beginners#tic-tac-toe-python-project
# visualisation task https://www.youtube.com/watch?v=8ext9G7xspg&t=2153s

# make two method to display what position player want and mwthod to calculate user input/move

# --- first version

filledPosition = {}
winning_rule = {
	"123",	"456",
	"789",	"147",
	"258",	"369",
	"159",	"357"
}

def display():
	line = ""
	dataPosition = {
		"2":"1",
		"4":"2",
		"6":"3",
		"9":"4",
		"11":"5",
		"13":"6",
		"16":"7",
		"18":"8",
		"20":"9"
	}
	i = 1

	for x in range(1, 22, +1):

		if i % 2 == 0:

			if dataPosition[str(x)] in filledPosition:

				if filledPosition[dataPosition[str(x)]] == "cpu":
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

def get_unfilled_position():
	for x in range(1, 10, +1):
		if str(x) not in filledPosition:
			return x
	return 0

def cpu_calculate(position):

	if position == 1:
		if str(2) not in filledPosition:
			filledPosition.update({"2" : "cpu"})
		elif str(5) not in filledPosition:
			filledPosition.update({"5" : "cpu"})
		elif str(4) not in filledPosition:
			filledPosition.update({"4" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})
	elif position == 2:
		if str(1) not in filledPosition:
			filledPosition.update({"1" : "cpu"})
		elif str(3) not in filledPosition:
			filledPosition.update({"3" : "cpu"})
		elif str(4) not in filledPosition:
			filledPosition.update({"4" : "cpu"})
		elif str(5) not in filledPosition:
			filledPosition.update({"5" : "cpu"})
		elif str(6) not in filledPosition:
			filledPosition.update({"6" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})
	elif position == 3:
		if str(2) not in filledPosition:
			filledPosition.update({"2" : "cpu"})
		elif str(5) not in filledPosition:
			filledPosition.update({"5" : "cpu"})
		elif str(6) not in filledPosition:
			filledPosition.update({"6" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})
	elif position == 4:
		if str(1) not in filledPosition:
			filledPosition.update({"1" : "cpu"})
		elif str(2) not in filledPosition:
			filledPosition.update({"2" : "cpu"})
		elif str(5) not in filledPosition:
			filledPosition.update({"5" : "cpu"})
		elif str(8) not in filledPosition:
			filledPosition.update({"8" : "cpu"})
		elif str(7) not in filledPosition:
			filledPosition.update({"7" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})
	elif position == 5:
		if str(1) not in filledPosition:
			filledPosition.update({"1" : "cpu"})
		elif str(2) not in filledPosition:
			filledPosition.update({"2" : "cpu"})
		elif str(3) not in filledPosition:
			filledPosition.update({"3" : "cpu"})
		elif str(4) not in filledPosition:
			filledPosition.update({"4" : "cpu"})
		elif str(6) not in filledPosition:
			filledPosition.update({"6" : "cpu"})
		elif str(7) not in filledPosition:
			filledPosition.update({"7" : "cpu"})
		elif str(8) not in filledPosition:
			filledPosition.update({"8" : "cpu"})
		elif str(9) not in filledPosition:
			filledPosition.update({"9" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})
	elif position == 6:
		if str(3) not in filledPosition:
			filledPosition.update({"3" : "cpu"})
		elif str(2) not in filledPosition:
			filledPosition.update({"2" : "cpu"})
		elif str(5) not in filledPosition:
			filledPosition.update({"5" : "cpu"})
		elif str(8) not in filledPosition:
			filledPosition.update({"8" : "cpu"})
		elif str(9) not in filledPosition:
			filledPosition.update({"9" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})
	elif position == 7:
		if str(4) not in filledPosition:
			filledPosition.update({"4" : "cpu"})
		elif str(5) not in filledPosition:
			filledPosition.update({"5" : "cpu"})
		elif str(8) not in filledPosition:
			filledPosition.update({"8" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})
	elif position == 8:
		if str(4) not in filledPosition:
			filledPosition.update({"4" : "cpu"})
		elif str(5) not in filledPosition:
			filledPosition.update({"5" : "cpu"})
		elif str(6) not in filledPosition:
			filledPosition.update({"6" : "cpu"})
		elif str(7) not in filledPosition:
			filledPosition.update({"7" : "cpu"})
		elif str(9) not in filledPosition:
			filledPosition.update({"9" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})
	elif position == 9:
		if str(5) not in filledPosition:
			filledPosition.update({"5" : "cpu"})
		elif str(6) not in filledPosition:
			filledPosition.update({"6" : "cpu"})
		elif str(8) not in filledPosition:
			filledPosition.update({"8" : "cpu"})
		elif get_unfilled_position() == 0:
			return "Its tie"
		else:
			filledPosition.update({str(get_unfilled_position()) : "cpu"})

def is_winning2():
	if len(filledPosition) == 0:
		return False

	cpu = set()
	player = set()
	for x in filledPosition:
		if filledPosition[x] == "cpu":
			cpu.add(x)
		elif filledPosition[x] == "player":
			player.add(x)

	for x in winning_rule:
		temp = set(x)
		temp_cpu = temp.intersection(cpu)
		temp_player = temp.intersection(player)

		if len(temp_cpu) == 3:
			return True
		elif len(temp_player) == 3:
			return True

	return False



isStop = False
print(display())
while isStop == False:
	ins = input("Your Move -> ")

	if int(ins):

		if ins in filledPosition:
			print("already exist")
			print(display())
			continue

		filledPosition.update({ins : "player"})
		print(display())

		if is_winning2():
			print("Player won")
			break

		cpu_calculate(int(ins))
		print(display())

		if is_winning2():
			print("CPU won")
			break

	else:
		isStop = True


#|1|2|3|
#|4|5|6|
#|7|8|9|	