import pygame
from pygame.locals import *

from textManager import TextManager

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255,255,255)

class Game:
	def __init__(self):
		self.window = pygame.display.set_mode((800, 600))
		self.quit = False

		self.title = TextManager("Le Couteau Sif")
		# dialogBox
		self.dialogBox = TextManager("Bonjour étrangé.") 
	
	def gameInit(self) -> None:
		#first text
		pass

	def gameLoop(self) -> None:
		self.gameInit()
		while not self.quit:
			self.eventManager()
			self.window.fill(BLACK)
			# draw
			self.drawText(self.title, 20, 20)
			self.drawText(self.dialogBox, 20, 600-60)
			pygame.display.update()

	def drawText(self, text:TextManager, posX:float, posY: float) -> None:
		self.window.blit(text.getTexture(), (posX, posY))

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
