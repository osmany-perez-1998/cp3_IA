# Player Template
# IMPORTANT: 	This module must have a function called play
# 				that receives a game and return a tuple of
#				two integers who represent a valid move on
#				the game.

import queue
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


def play(game, player):
	# Code Here
	# Random player implementation (just delete it)

	return minimax(game, player, 3, heuristic, moves)


def moves(game, player):
	for x in range(game.size):
		for y in range(game.size):
			if game[x, y] == EMPTY:
				yield (x, y)


def heuristic(game, player):
	return 1 - (bfs(game,player)/(game.size**2))


def desired_neighbour(game:Game, player,x,y):
	for i,j in game.neighbour(x, y):
		if game[i,j] == EMPTY or game[i,j]== player:
			yield (i,j)


def bfs(game:Game,player):
	q = []
	v = {}


	for j in range(game.size):
		a,b =j,0
		if player == PLAYER[1]:
			a,b = 0,j
		
		if game[a,b] == EMPTY:
			q.append(((a,b),1,None))
			v[(a,b)]=(1,None)
		elif game[a,b] == player:
			q.append(((a,b),0,None))
			v[(a,b)]=(0,None)
			

	while q:
		place = q.pop(0)

		x,y = place[0]
		if place[0][1 if player == PLAYER[0] else 0] == game.size -1:
			return place[1]

		aux =[]
		for neig in desired_neighbour(game,player,x,y):
			try:
				v[neig]
			except KeyError:
				if game[neig[0],neig[1]] == EMPTY:
					aux.append(((neig[0],neig[1]),place[1]+1, place[0]))
					v[neig] = (place[1]+1,place[0])
				else:
					aux.insert(0,((neig[0],neig[1]),place[1], place[0]))					
					v[neig] = (place[1],place[0])					
		
		q.extend(aux)	

	

	







	

	
	

