"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
"""
import random
import os

def clear_screen():
	
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")


def validate_input(prompt, valid_inputs):

	valid = False
	while not valid : 
		res = input(prompt)
		valid = valid_inputs[int(res)-1]
	return int(res)


def create_board():

	board = []
	for i in range(6):
		row = []
		for i in range(7):
			row.append(0)
		board.append(row)
	return board


def print_board(board):
	
	print(" 1  2  3  4  5  6  7")
	print("_____________________")
	for row in board:
		print(row)

def drop_piece(board, player, column):
	
	for i in range(len(board[0])):
		if board[len(board)-(1+i)][column-1] == 0:
			board[len(board)-(1+i)][column-1] = player
			return True
	return False

def execute_player_turn(player, board):
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	print("it is " + str(player) + "'s turn")
	print_board(board)
	input = validate_input("Choose a collom: ",get_valid_inputs(board))
	return drop_piece(board, player, input)

def get_valid_inputs(board):
	"""
	returns a list of 
	"""
	valid_inputs = []
	for i in range(len(board[0])):
		if board[0][i] == 0: 
			valid_inputs.append(True)
		else:
			valid_inputs.append(False)
	return valid_inputs

def collect_diags(board):
	r = 5
	c = 0
	while True:
		row = r
		collum = c
		while row <= 5 and collum <= 6:
			row += 1
			collum += 1
			


def coollect_arrs():
	#this is the array that all lists are collected in
	arra = collect_diags
	#collects all rows
	for i in len(create_board):
		arra.append(i)

	#collects all columns
	for i in range(len(create_board[0])):
		new_list = []
		for j in range(len(create_board)):
			new_list.append(create_board[j][i])
		arra.append(new_list)
	print(len(arra))
	return arra

def for_in_a_row(arra):
	count = 3
	for i in range(len(arra)-1):
		if arra[i] == arra[i+1]:
			count -= 1
		else:
			count = 3
		if count == 0:
			return arra[i] 
	return
		
def end_of_game(board, player):
	"""
	Checks if the game has ended with a winner
	or a draw.

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""
	arra = coollect_arrs(board)
	for i in range(len(arra)):
		if end_of_game == 1 or end_of_game == 2:
			return player
	valid = get_valid_inputs(board)
	valid = [not elem for elem in valid]
	if all(valid) == True:
		return 3
		


def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	print_rules()
	#make a board
	board = create_board()
	#set player to 1
	player  = 1
	#runs a loop forever
	while True:
		#does turn of player
		execute_player_turn(player, board)
		#checks if game is done
		game_status = end_of_game(board, player)
		#break condition for while loop
		if game_status == 1 or game_status == 2:
			# sees who wins
			print(f"player {game_status} wins!")
			# ends the while loop
			break
		if game_status == 3:
			print("it is a draw")
			break
		#switches the player turn
		if player == 1: player += 1
		else: player -= 1



def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	raise NotImplementedError


def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty. 
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	raise NotImplementedError


def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	This function creates a copy of the board to simulate moves.
	<Insert player strategy here>

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	raise NotImplementedError


def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


if __name__ == "__main__":
	# main()
	local_2_player_game()




