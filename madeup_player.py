# Player Template
# IMPORTANT: 	This module must have a function called play
# 				that receives a game and return a tuple of
#				two integers who represent a valid move on
#				the game.

from game_logic import *
from minimax import minimax

# game_logic
#
# 	EMPTY		
#	PLAYER[0]	
#	PLAYER[1]

# game
# 	-> current (W or B)
#		It refers to the player who must play in
#		this turn.
#	-> indexing
#		game[i,j] return the player who have played
#		on position <i;j> (compare with PLAYER[0] 
#		and PLAYER[1]). EMPTY if none player have
#		played there.
#	-> neighbour
#		creates an iterator that yields all 
#		coordinates <x;y> who are neighbour of 
#		current coordinates.
#
#		for nx, ny in game.neighbour(x, y):
#			print(nx, ny)


def play(game:Game, player):
	# Code Here
	# Random player implementation (just delete it)
    # current_score = -1
    # move = None
    # for x,y in moves(game, player):
    #     game1 = game.clone_play(x,y)

    #     heur = heuristic(game1,player)
    #     if heur <current_score or current_score ==-1:
    #         current_score = heur
    #         move = (x,y)
<<<<<<< HEAD
    # return move
    return minimax(game, player, 3, heuristic, moves)
=======

    # return move
	return minimax(game, player, 3, heuristic, moves)
>>>>>>> 9decd19a173f13c784f8bbc3496919d4a748511c


def moves(game, player):
	for x in range(game.size):
		for y in range(game.size):
			if game[x, y] == EMPTY:
				yield (x, y)


def heuristic(game:Game, player):
    rel_compo = 1
    empty_lines = 0
    
    for i in range(game.size):

        free_line = True
        for j in range(game.size):
            # Swap if B is playing in order to search by rows, not columns
            x,y = i,j
            if player == PLAYER[1]:
                x,y=y,x

            if game[x,y] == player:
                free_line = False

                if game.ds[game.position(x,y)] == -1:
                    rel_compo += 1        
        
        empty_lines+=free_line 

    return empty_lines - (1/rel_compo)