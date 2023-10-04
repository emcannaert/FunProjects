#! /usr/bin/env python

import sys, os

def get_input(player,board):

	"""
	playable tic-tac-toe game
	run with python3 TicTacToe.py
	I was writing a lot of C++/C code before this, so many of the var names are camal case ...
	"""
	invalidInput = True
	newMoveRow = -999
	newMoveColumn = 999
	mapper =  {'A' : 0, 'B': 1, 'C':2 , 'a':0,'b':1,'c':2  }
	while invalidInput:
		invalidInput = False # (after check of input)
		move = input("Player %s: please enter a row letter (A-C) and column number (1-3) (EX. A2, C3).  "%player)
		if len(move) != 2:
			print("Please only input two characters: <Letter><Number> for letters A-C and number 1-3")
			invalidInput = True
		elif not (   (ord(move[0]) < 68 and ord(move[0]) > 64  ) or ( ord(move[0]) > 96 and ord(move[0]) < 100  ) ):
			print("First character must be a letter between A and C.")
			invalidInput = True
		elif not move[1].isdigit():
			print("Second character must be a number (between 1 and 3).")
			invalidInput = True
		elif int(move[1]) > 3 or int(move[1]) < 1:
			print("Second character must be a number between 1 and 3.")
			invalidInput = True
		elif board[ mapper[move[0]]][int(move[1]) -1 ] != ' ':
			print("This square has already been claimed. Please choose an empty square.")
			invalidInput = True

	newMoveRow = mapper[move[0]]
	newMoveColumn = int(move[1]) -1 

	return newMoveRow,newMoveColumn
def draw_board(board,newMoveRow,newMoveColumn,player):


	# change new move right here so the board is updated
	if player == 0:
		board[newMoveRow][newMoveColumn] = "X"
	elif player == 1:
		board[newMoveRow][newMoveColumn] = "O"
	else:
		print("Something is fucky ...")

	print("")
	print("     1    2    3")
	print("    _____________")
	print("A   | %s | %s | %s |"%(board[0][0],board[0][1],board[0][2]))
	print("B   | %s | %s | %s |"%(board[1][0],board[1][1],board[1][2]))
	print("C   | %s | %s | %s |"%(board[2][0], board[2][1],board[2][2]))
	print("    _____________")

def check_is_done(board):
	#check horizontally, check vertically, check diagonals
	
	for iii in range(0,3):
		rowToCheck = [val for val in board[iii]] # apparently this can just be list(board[iii])
		colToCheck = [val[iii] for val in board]
		if "X_X_X" in '_'.join(rowToCheck):
			return True, 'Player 0'
		if 'X_X_X' in '_'.join(colToCheck):
			return True,'Player 0'
		if 'O_O_O' in '_'.join(rowToCheck):
			return True,'Player 1'
		if 'O_O_O' in '_'.join(colToCheck):
			return True,'Player 1'

	if 'X_X_X' in '%s_%s_%s'%(board[0][0], board[1][1],board[2][2]):
		return True, 'Player 0'
	if "O_O_O" in '%s_%s_%s'%(board[0][0], board[1][1],board[2][2]):
		return True, 'Player 1'

	# if all spots are taken, end game as a draw.
	if not any(' ' in sublist for sublist in board):
		return True, "nobody - all squares full, game ends as a draw"
	return False, ""
def play_game():
	isDone = False
	board = [     [' ', ' ', ' '],  
			      [' ', ' ', ' '],
			      [' ', ' ', ' ']] 
	winner = [-999]
	counter = 0
	while not isDone:
		player = counter%2   # 0 == player 1 (Xs), 1 == player 2 (Os)
		newMoveRow,newMoveColumn = getInput(player,board)
		drawBoard(board,newMoveRow,newMoveColumn,player)
		isDone, winner[0] = check_is_done(board)
		counter+=1 
	print("Winner is %s."%winner[0])
	print("Thanks for playing!")

def main(args):
	play_game()


if __name__ == "__main__":
    main(sys.argv[1:])