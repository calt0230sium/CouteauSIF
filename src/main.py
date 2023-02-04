import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

class Game:
	def __init__(self):
		self.window = pygame.display.set_mode((400, 500))
		self.quit = False

	def gameLoop(self) -> None:
		while not self.quit:
			self.eventManager()

	def eventManager(self) -> None:
		for event in pygame.event.get():

			match event.type:
				
				case pygame.KEYDOWN:
					self.shortcut(event.key)

				case pygame.MOUSEBUTTONDOWN:
					self.mouseManager(event.button)

				case pygame.QUIT:
					print("quit !")
					self.quit = True

	def shortcut(self, event_key) -> None:
		match event_key:

			case pygame.K_SPACE:
				print("interaction espace !")

	def mouseManager(self, event_mouse) -> None:
		print(pygame.mouse.get_pos())

CouteauSIF = Game()
CouteauSIF.gameLoop()