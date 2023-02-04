import pygame
from pygame.locals import *

from textManager import TextManager
from scenes.scene_test import Scene_test

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

		self.current_scene = 1

		# all the scene
		self.scene_test = Scene_test(self.window)

		# texts
		self.title = TextManager("Le Couteau Sif", False)
		self.dialogBox = TextManager("Bonjour étrangé.", True) 
	
	def gameInit(self) -> None:
		#time
		self.time = pygame.time.Clock()

		#draw first frame
		pygame.display.flip()

	def showScene(self) -> None:
		match self.current_scene:
			case 1:
				self.title.initialize()
				self.drawText(self.title, 800/2, 600/2)
			case _:
				self.scene_test.update()

	def gameLoop(self) -> None:
		self.gameInit()

		while not self.quit:
			# event
			self.eventManager()
			
			# draw
			self.showScene()
			
			#draw next
			pygame.display.flip()

			# update clock
			self.time.tick()

	def drawText(self, text:TextManager, posX:float, posY: float) -> None:
		self.window.blit(text.getTexture(pygame.time.get_ticks()), (posX, posY))

	def eventManager(self) -> None:
		for event in pygame.event.get():
			match event.type:
				case pygame.QUIT:
					print("quit !")
					self.quit = True

				case pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.current_scene = 2

CouteauSIF = Game()
CouteauSIF.gameLoop()
