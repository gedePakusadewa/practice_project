# https://www.freecodecamp.org/news/python-projects-for-beginners#tic-tac-toe-python-project
# visualisation task https://www.youtube.com/watch?v=8ext9G7xspg&t=2153s

# make two method to display what position player want and mwthod to calculate user input/move

# --- second version

class TicTacToeGame():
	winning_rule_set = {
		"123",	"456",
		"789",	"147",
		"258",	"369",
		"159",	"357"
	}
	number_position_map = {
		2:1,
		4:2,
		6:3,
		9:4,
		11:5,
		13:6,
		16:7,
		18:8,
		20:9
	}

	player_1 = "cpu"
	player_2 = "sandi"
	border_grid = "|"
	empty_content_grid = "-"
	player_1_cursor = "X"
	player_2_cursor = "O"
	draw_message = "Its a tie"
	exist_position_message = "Invalid position"
	won_message = "XXX won"

	def __init__(self):
		self.curr_user_input = 0
		self.filled_position = {}
		self.is_stop = False

	# ini hanya mencari yg kosong bukan mencari posisi yg paling berpotensi bisa menang
	# cari cara biar cpu tau mana posisi yg paling menguntungkan
	def get_unfilled_position(self):
		for x in self.number_position_map:
			if self.number_position_map[x] not in self.filled_position:
				return self.number_position_map[x]
		return 0

	def is_win(self):
		if len(self.filled_position) == 0:
			return False

		player1_positions = set()
		player2_positions = set()
		for x in self.filled_position:
			if self.filled_position[x] == self.player_1:
				player1_positions.add(str(x))
			elif self.filled_position[x] == self.player_2:
				player2_positions.add(str(x))

		for x in self.winning_rule_set:
			temp = set(x)
			temp_player1 = temp.intersection(set(player1_positions))
			temp_player2 = temp.intersection(set(player2_positions))

			if len(temp_player1) == 3:
				return True
			elif len(temp_player2) == 3:
				return True

		return False

	def is_draw(self):
		if len(self.filled_position) == 9:
			return True

		return False

	def display_grid(self):
		grid = ""
		i = 1

		for x in range(1, 22, +1):
			if i % 2 == 0:
				if self.number_position_map[x] in self.filled_position:
					if self.filled_position[self.number_position_map[x]] == self.player_1:
						grid += self.player_1_cursor
					else:
						grid += self.player_2_cursor
				else:
					grid += self.empty_content_grid
			else:
				grid += self.border_grid

			if x % 7 == 0:
				grid += "\n"
				i = 0

			i += 1

		return grid

	def calculate_next_move(self):
		if self.curr_user_input == 1:
			if 2 not in self.filled_position:
				self.filled_position.update({2 : self.player_1})
			elif 5 not in self.filled_position:
				self.filled_position.update({5 : self.player_1})
			elif 4 not in self.filled_position:
				self.filled_position.update({4 : self.player_1})
			else:
				self.filled_position.update({self.self.get_unfilled_position() : self.player_1})
		elif self.curr_user_input == 2:
			if 1 not in self.filled_position:
				self.filled_position.update({1 : self.player_1})
			elif 3 not in self.filled_position:
				self.filled_position.update({3 : self.player_1})
			elif 4 not in self.filled_position:
				self.filled_position.update({4 : self.player_1})
			elif 5 not in self.filled_position:
				self.filled_position.update({5 : self.player_1})
			elif 6 not in self.filled_position:
				self.filled_position.update({6 : self.player_1})
			else:
				self.filled_position.update({self.get_unfilled_position : self.player_1})
		elif self.curr_user_input == 3:
			if 2 not in self.filled_position:
				self.filled_position.update({2 : self.player_1})
			elif 5 not in self.filled_position:
				self.filled_position.update({5 : self.player_1})
			elif 6 not in self.filled_position:
				self.filled_position.update({6 : self.player_1})
			else:
				self.filled_position.update({self.get_unfilled_position() : self.player_1})
		elif self.curr_user_input == 4:
			if 1 not in self.filled_position:
				self.filled_position.update({1 : self.player_1})
			elif 2 not in self.filled_position:
				self.filled_position.update({2 : self.player_1})
			elif 5 not in self.filled_position:
				self.filled_position.update({5 : self.player_1})
			elif 8 not in self.filled_position:
				self.filled_position.update({8 : self.player_1})
			elif 7 not in self.filled_position:
				self.filled_position.update({7 : self.player_1})
			else:
				self.filled_position.update({self.get_unfilled_position() : self.player_1})
		elif self.curr_user_input == 5:
			if 1 not in self.filled_position:
				self.filled_position.update({1 : self.player_1})
			elif 2 not in self.filled_position:
				self.filled_position.update({2 : self.player_1})
			elif 3 not in self.filled_position:
				self.filled_position.update({3 : self.player_1})
			elif 4 not in self.filled_position:
				self.filled_position.update({4 : self.player_1})
			elif 6 not in self.filled_position:
				self.filled_position.update({6 : self.player_1})
			elif 7 not in self.filled_position:
				self.filled_position.update({7 : self.player_1})
			elif 8 not in self.filled_position:
				self.filled_position.update({8 : self.player_1})
			elif 9 not in self.filled_position:
				self.filled_position.update({9 : self.player_1})
			else:
				self.filled_position.update({self.get_unfilled_position() : self.player_1})
		elif self.curr_user_input == 6:
			if 3 not in self.filled_position:
				self.filled_position.update({3 : self.player_1})
			elif 2 not in self.filled_position:
				self.filled_position.update({2 : self.player_1})
			elif 5 not in self.filled_position:
				self.filled_position.update({5 : self.player_1})
			elif 8 not in self.filled_position:
				self.filled_position.update({8 : self.player_1})
			elif 9 not in self.filled_position:
				self.filled_position.update({9 : self.player_1})
			else:
				self.filled_position.update({self.get_unfilled_position() : self.player_1})
		elif self.curr_user_input == 7:
			if 4 not in self.filled_position:
				self.filled_position.update({4 : self.player_1})
			elif 5 not in self.filled_position:
				self.filled_position.update({5 : self.player_1})
			elif 8 not in self.filled_position:
				self.filled_position.update({8 : self.player_1})
			else:
				self.filled_position.update({self.get_unfilled_position() : self.player_1})
		elif self.curr_user_input == 8:
			if 4 not in self.filled_position:
				self.filled_position.update({4 : self.player_1})
			elif 5 not in self.filled_position:
				self.filled_position.update({5 : self.player_1})
			elif 6 not in self.filled_position:
				self.filled_position.update({6 : self.player_1})
			elif 7 not in self.filled_position:
				self.filled_position.update({7 : self.player_1})
			elif 9 not in self.filled_position:
				self.filled_position.update({9 : self.player_1})
			else:
				self.filled_position.update({self.get_unfilled_position() : self.player_1})
		elif self.curr_user_input == 9:
			if 5 not in self.filled_position:
				self.filled_position.update({5 : self.player_1})
			elif 6 not in self.filled_position:
				self.filled_position.update({6 : self.player_1})
			elif 8 not in self.filled_position:
				self.filled_position.update({8 : self.player_1})
			else:
				self.filled_position.update({self.get_unfilled_position() : self.player_1})

	def smart_cpu(self):
		

	def run(self):
		print(self.display_grid())

		while self.is_stop == False:
			ins = input("Your Move -> ")

			if int(ins) in self.filled_position:
				print(self.exist_position_message)
				print(self.display_grid())
				continue

			if int(ins):
				temp_inp = int(ins)
				self.curr_user_input = temp_inp
				self.filled_position.update({temp_inp : self.player_2})
				print(self.display_grid())

				if self.is_draw():
					print(self.draw_message)
					break

				if self.is_win():
					print(self.won_message.replace("XXX", self.player_2.upper()))
					break

				self.calculate_next_move()
				print(self.display_grid())

				if self.is_draw():
					print(self.draw_message)
					break

				if self.is_win():
					print(self.won_message.replace("XXX", self.player_1.upper()))
					break
				print(self.filled_position)
			else:
				self.is_stop = True

tes = TicTacToeGame()
tes.run()