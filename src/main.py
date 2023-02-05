import pygame
from pygame.locals import *

from textManager import TextManager
from scenes.scene_test import Scene_test
from scenes.scenar import Scene_chat

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255,255,255)

EPIC_SOUND = pygame.mixer.Sound('../assets/sounds/epic.mp3')
SCREAM_SOUND = pygame.mixer.Sound('../assets/sounds/cri.mp3')

SUCESS_SOUND = pygame.mixer.Sound('../assets/sounds/succes.mp3')
MIAOU_SOUND = pygame.mixer.Sound('../assets/sounds/miaou.mp3')
SIFFLET_SOUND = pygame.mixer.Sound('../assets/sounds/sifflet.mp3')
TEL_SOUND = pygame.mixer.Sound('../assets/sounds/telephone.mp3')
LAME_SOUND_1 = pygame.mixer.Sound('../assets/sounds/changement_lame.mp3')
LAME_SOUND_2 = pygame.mixer.Sound('../assets/sounds/changement_lame2.mp3')
METAL_SOUND = pygame.mixer.Sound('../assets/sounds/coup_metallique.mp3')
COUP_DE_COUTEAU = pygame.mixer.Sound('../assets/sounds/coup_de_couteau.mp3')

MENU = pygame.image.load('../assets/menu/menu.png')
REGLES0 = pygame.image.load('../assets/menu/regles0.png')
REGLES = pygame.image.load('../assets/menu/regles.png')

MANCHE = [pygame.image.load('../assets/menu/couteau1.png'),
pygame.image.load('../assets/menu/couteau2.png'),
pygame.image.load('../assets/menu/couteau3.png'),
pygame.image.load('../assets/menu/couteau4.png')]

CLASSIC_MODE = pygame.image.load('../assets/menu/mode_classique.png')
RANDOM_MODE = pygame.image.load('../assets/menu/mode_random.png')

FIN_MINOU = pygame.image.load('../assets/menu/fin_miaou.png')

GAME_MODE = "CLASSIQUE"
CAT_NB = 0

INVENTAIRE = pygame.image.load('../assets/inventaires/Inventaire_1.png')

COUTEAUX = [
	pygame.image.load('../assets/couteau/vide.png'),
	pygame.image.load('../assets/couteau/couteau.png'),
	pygame.image.load('../assets/couteau/laser_full.png'),
	pygame.image.load('../assets/couteau/sifflet.png'),
	pygame.image.load('../assets/couteau/tournevis.png'),
	pygame.image.load('../assets/couteau/clef.png'),

	# à part
	pygame.image.load('../assets/couteau/briquet_off.png'),
	pygame.image.load('../assets/couteau/briquet_on.png'),
	pygame.image.load('../assets/couteau/couteau_sang.png'),
	pygame.image.load('../assets/couteau/tournevis_cassé.png'),
	pygame.image.load('../assets/couteau/laser_vide.png'),
	pygame.image.load('../assets/couteau/laser_moitié.png'),
]

class Controls:
	def __init__(self):
		self.buttonRight = False
		self.buttonLeft = False
		self.space = False
		self.space_once = False
		self.valid = True

	def updateSpaceOnceKeyDown(self) -> None:
		if not self.valid:
			self.space_once = False
		if self.space:
			if self.valid:
				self.space_once = True
			self.valid = False

	def updateSpaceOnceKeyUp(self) -> None:
		self.space_once = False
		self.valid = True


class Player:
	def __init__(self):
		self.knifeState = 0
		self.knifeFunctionnality = [
			"none",
			"couteau",
			"laser",
			"sifflet",
			"tournevis",
			"clé",
		]
		self.actionTrigger = False

	def action(self) -> str:
		return self.knifeFunctionnality[self.knifeState]

	def isActionTriggered(self) -> bool:
		return self.actionTrigger

class Game:
	def __init__(self):
		self.window = pygame.display.set_mode((800, 600))
		pygame.display.set_caption('Couteau SIF - Chapitre 1')

		pygame.mixer.init()
		pygame.mixer.music.load('../assets/loop.mp3')
		pygame.mixer.music.play(-1)

		self.controls = Controls()
		self.player = Player()
		
		self.quit = False

		self.current_scene_id = 0
		self.currentScene = None

		# title screen
		self.title = TextManager("Le Couteau Sif", 50, False)
		# root scene
		self.root = Scene_test(self.window, self.player)

		self.title = TextManager("Le Couteau Sif", 60, False)
		self.chapter = TextManager("Chapitre 1", 60, False)

	def gameInit(self) -> None:
		#time
		self.time = pygame.time.Clock()

		#draw first frame
		pygame.display.flip()

	def showScene(self) -> None:
		match self.current_scene_id:
			case -1: #Fin cachée
				self.window.blit(FIN_MINOU, (0, 0))

			case 0: # menu
				self.window.blit(MENU, (0, 0))
				x, y = pygame.mouse.get_pos()
				if 200 < y < 500 :
					if 50 < x < 350 :
						self.window.blit(CLASSIC_MODE, (20, 105))
					if 450 < x < 750 :
						self.window.blit(RANDOM_MODE, (370, 200))
				self.window.blit(MANCHE[pygame.time.get_ticks()//200%4], (270, 450))

			case 1: # title
				self.window.blit(REGLES0, (0, 0))

			case 2: # title
				self.window.blit(REGLES, (0, 0))

			case 3: # title
				self.title.initialize()
				self.drawText(self.title, 800/2-150, 600/2-20)

			case 4: # title
				self.title.initialize()
				self.drawText(self.chapter, 800/2-125, 600/2-20)

			case 5: # other scene
				self.window.blit(INVENTAIRE, (600, 0))

				self.window.blit(COUTEAUX[self.player.knifeState], (600, 80))

				if self.currentScene is None:
					self.currentScene = self.root

				if self.currentScene.sceneTools.sceneTransition() is not None: # on veut changer de scène
					self.currentScene = self.currentScene.sceneTools.sceneTransition()

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
		self.window.blit(
			text.getTexture(pygame.time.get_ticks()), (posX, posY)
		)

	def eventManager(self) -> None:
		for event in pygame.event.get():
			match event.type:
				case pygame.QUIT:
					print("quit !")
					self.quit = True

				case pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						if self.current_scene_id == 4:
							pygame.mixer.music.play(-1)
							self.current_scene_id = 5
						if self.current_scene_id == 3:
							pygame.mixer.Sound.play(EPIC_SOUND)
							pygame.mixer.Sound.play(SCREAM_SOUND)
							self.current_scene_id = 4
						if self.current_scene_id == 2:
							pygame.mixer.music.stop()
							pygame.mixer.Sound.play(EPIC_SOUND)
							self.current_scene_id = 3
						if self.current_scene_id == 1:
							self.current_scene_id = 2
						
						if self.current_scene_id == 0:
							self.current_scene_id = 1
						self.controls.space = True

				case pygame.KEYUP:
					if event.key == pygame.K_SPACE:
						self.controls.space = False
						self.controls.updateSpaceOnceKeyUp()

				case pygame.MOUSEBUTTONDOWN:
					if event.button == pygame.BUTTON_LEFT:
						self.player.actionTrigger = True

						if self.current_scene_id == 0:
							global GAME_MODE
							x, y = pygame.mouse.get_pos()
							if 200 < y < 500 :
								if 50 < x < 350 :
									GAME_MODE = "CLASSIQUE"
									pygame.mixer.Sound.play(LAME_SOUND_1)
									self.current_scene_id = 1
								if 450 < x < 750 :
									GAME_MODE = "RANDOM"
									self.current_scene_id = 1
									pygame.mixer.Sound.play(LAME_SOUND_2)
							if x < 80 and y > 520 :
								pygame.mixer.Sound.play(SUCESS_SOUND)
								self.quit = True
							if x > 720 and y > 520 :
								global CAT_NB
								CAT_NB += 1
								if CAT_NB >= 1000 and self.current_scene_id != -1 :
									self.current_scene_id = -1
									pygame.mixer.Sound.play(SUCESS_SOUND)
								pygame.mixer.Sound.play(MIAOU_SOUND)

				case pygame.MOUSEBUTTONUP:
					if event.button == pygame.BUTTON_LEFT:
						self.player.actionTrigger = False

				case pygame.MOUSEWHEEL:
					if self.current_scene_id >= 5:
						self.player.knifeState = (self.player.knifeState + event.y)%(len(self.player.knifeFunctionnality))
						print(self.player.action())

		self.controls.updateSpaceOnceKeyDown()

CouteauSIF = Game()
CouteauSIF.gameLoop()
