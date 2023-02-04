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


class Controls:
	def __init__(self):
		self.buttonRight = False
		self.buttonLeft = False
		self.space = False

class Game:
	def __init__(self):
		self.window = pygame.display.set_mode((800, 600))
		self.controls = Controls()
		self.quit = False

		self.current_scene_id = 0
		self.currentScene = None

		# all the scene
		self.bobine = [
			Scene_test(self.window, self.controls),
		]

		# texts
		self.title = TextManager("Le Couteau Sif", False)
		self.dialogBox = TextManager("Bonjour étrangé.", True) 
	
	def gameInit(self) -> None:
		#time
		self.time = pygame.time.Clock()

		#draw first frame
		pygame.display.flip()

	def showScene(self) -> None:
		match self.current_scene_id:
			case 0: # title
				self.title.initialize()
				self.drawText(self.title, 800/2, 600/2)
			case _: # other scene
				if self.currentScene is not self.bobine[self.current_scene_id-1]:
					self.currentScene = self.bobine[self.current_scene_id-1]

				self.currentScene.update()

	def gameLoop(self) -> None:
		self.gameInit()
		while not self.quit:
			# event
			self.eventManager()
			
			# draw
			self.window.fill(BLACK)
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
						if self.current_scene_id == 0:
							self.current_scene_id = 1
						self.controls.space = True

				case pygame.KEYUP:
					if event.key == pygame.K_SPACE:
						self.controls.space = False

				case pygame.MOUSEBUTTONDOWN:
					if event.button == pygame.BUTTON_RIGHT:
						self.controls.buttonRight = True
					if event.button == pygame.BUTTON_LEFT:
						self.controls.buttonLeft = True

				case pygame.MOUSEBUTTONDOWN:
					if event.button == pygame.BUTTON_RIGHT:
						self.controls.buttonRight = False
					if event.button == pygame.BUTTON_LEFT:
						self.controls.buttonLeft = False

CouteauSIF = Game()
CouteauSIF.gameLoop()
