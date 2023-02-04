import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255,255,255)

class TextManager:
	def __init__(self, text:str, splitText:bool) -> None:
		self.currentTxt = ""
		self.currentWord = 0
		self.font = pygame.font.SysFont(None, 48)

		self.txt = text
		self.splitText = splitText

		self.isInitialized = False

	def initialize(self) -> None:
		if self.splitText and (not self.isInitialized):
			# init all texture
			self.allTexture = []

			if self.splitText:
				for i in range(len(self.txt)):
					self.allTexture.append(self.font.render(self.txt[0:i], True, WHITE))
			
			self.isInitialized = True

	def setText(self, text:str) -> None:
		self.txt = text

	def getTexture(self, time:float) -> pygame.Surface:
		if (self.splitText):

			if time%5 == 0:
				self.currentWord = self.currentWord + 1
			
			tex_id = 0
			if self.currentWord < len(self.txt):
				tex_id = self.currentWord
			else:
				self.currentWord = 0

			return self.allTexture[tex_id]
		else:
			return self.font.render(self.txt, True, WHITE)