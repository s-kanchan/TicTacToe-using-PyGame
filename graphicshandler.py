import sys
import pygame

class GraphicsHandler:

	_bg_color = (255, 255, 255)
	black = (0, 0, 0)
	screen = None

	@staticmethod
	def initialize_board(_type = 1):

		#pygame.init()
		#GraphicsHandler.screen = pygame.display.set_mode(size)
		GraphicsHandler.screen.fill(GraphicsHandler._bg_color)
		if _type == 1:
			pygame.draw.line(GraphicsHandler.screen, GraphicsHandler.black, [200,50], [200,550], 5)
			pygame.draw.line(GraphicsHandler.screen, GraphicsHandler.black, [400,50], [400,550], 5)
			pygame.draw.line(GraphicsHandler.screen, GraphicsHandler.black, [50,200], [550,200], 5)
			pygame.draw.line(GraphicsHandler.screen, GraphicsHandler.black, [50,400], [550,400], 5)

		pygame.display.flip()

	@staticmethod
	def initialize_game(size = [600, 600]):
		pygame.init()
		GraphicsHandler.screen = pygame.display.set_mode(size)
		GraphicsHandler.screen.fill(GraphicsHandler._bg_color)
		font = pygame.font.Font(None, 35)
		text_title = font.render("TIC TAC TOE", 5, GraphicsHandler.black)
		title = GraphicsHandler.screen.blit(text_title, (200,100))
		pygame.display.flip()

		running = True

		while  running:
			event = pygame.event.poll()
			if event.type == pygame.QUIT: 
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				if title.collidepoint(mouse_pos):
					GraphicsHandler.initialize_board()
					running = False


