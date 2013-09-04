import sys
import pygame
#import GameManager from game_mgr
from graphicshandler import GraphicsHandler

def start_game():
	#GraphicsHandler.initialize_board()
	GraphicsHandler.initialize_game()
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				GraphicsHandler.initialize_board()


start_game()