# https://www.freecodecamp.org/news/python-projects-for-beginners#tic-tac-toe-python-project
# visualisation task https://www.youtube.com/watch?v=8ext9G7xspg&t=2153s

# make two method to display what position player want and mwthod to calculate user input/move

# --- third version

class Player():
	def __init__(self, letter):
		self.letter = letter

	def set_move(self):
		pass

class HumanPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def set_move(self, game):
		is_valid_move = False
		val = None
		while not is_valid_move:
			move = input("Type number from 0-8 -> ")

			try:
				val = int(move)
				if val not in game.available_moves():
					raise ValueError
				is_valid_move = True
			except ValueError:
				print("Invalid move")
		return val

class CPUPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def set_move(self, game):
		import random as rnd

		return rnd.choice(game.available_moves())

class TicTacToe():
	def __init__(self):
		#self.board ex value => [" ", "O", " ", " ", "X", " ", " ", "O", " "]
		#self.curr_winner ex value => O
		self.board = self.set_board()
		self.curr_winner = None

	@staticmethod
	def set_board():
		#output [" ", " ", " ", " ", " ", " ", " ", " ", " "]
		#|   |   |   |
		#|   |   |   |
		#|   |   |   |

		return [" " for _ in range(9)]

	def print_board(self):
		#output ex current
		#self.board => ["X", " ", " ", " ", " ", " ", " ", "O", " "]
		#| X |   |   |
		#|   |   |   |
		#|   | O |   |

		for row in [self.board[i*3:((i+1) * 3)]for i in range(3)]:
			print("| " + " | ".join(row) + " |")

	@staticmethod
	def print_board_nums():
		number_board = [[str(i) for i in range(j*3, (j+1)*3 )] for j in range(3)]
		for row in number_board:
			print("| " + " | ".join(row) + " |")

	def make_move(self, move, letter):
		if self.board[move] == " ":
			self.board[move] = letter
			if self.is_winner(move, letter):
				self.curr_winner = letter
			return True
		return False

	def is_winner(self, move, letter):
		import math

		#board tic tac toe index
		#| 0 | 1 | 2 |
		#| 3 | 4 | 5 |
		#| 6 | 7 | 8 |

		#ex board
		#| X |   | O |
		#|   |   |   |
		#|   | O | X |

		#find move is in what row in board 3x3, ex: row 0 OR row 2
		row_ind = math.floor(move / 3)
		#ex row 1 from ex board value ["X", " ", "O"]
		row = self.board[row_ind*3:(row_ind+1)*3]
		if all([s == letter for s in row]): 
			#if all letter in list row have value same as letter then that is a win
			return True

		#find what column is the "move", ex: col 0 OR col 2
		col_ind = move % 3
		#ex col 3 from ex board value ["O", " ", "X"]
		col = [self.board[col_ind + i*3] for i in range(3)]
		if all([s == letter for s in col]):
			return True

		#check if this move(index board) is diagonal(even number)
		if move % 2 == 0:
			diagonal1 = [self.board[i] for i in [0, 4, 8]]
			if all([s == letter for s in diagonal1]):
				return True

			diagonal2 = [self.board[i] for i in [2, 4, 6]]
			if all([s == letter for s in diagonal2]):
				return True

		return False

	def is_move_available(self):
		return " " in self.board

	def total_available_move(self):
		return self.board.count(" ")

	def available_moves(self):
		return [i for i, x in enumerate(self.board) if x == " "]

def play(game, x_player, o_player, print_game=True):
	import time

	if print_game:
		game.print_board_nums()

	letter = "X"
	while game.is_move_available():
		if letter == "O":
			move = o_player.set_move(game)
		else:
			move = x_player.set_move(game)

		if game.make_move(move, letter):
			if print_game:
				print(f"{letter} makes a move to square.")
				game.print_board()
				print('')

			if game.curr_winner:
				if print_game:
					print(letter + " wins!")

				return letter # end loop

			# switches player
			letter = 'O' if letter == 'X' else 'X'

	    # this is just a delay, this does not effect the code if u remove this
		time.sleep(.8)

    #if there are no move anymore and there is no winner
    #then this is a tie
	if print_game:
		print('It\'s a tie!')

if __name__ == '__main__':
    x_player = CPUPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)