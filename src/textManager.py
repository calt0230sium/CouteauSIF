import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255,255,255)

class TextManager:
	def __init__(self, text:str, fontsize:int, splitText:bool) -> None:
		self.currentTxt = ""
		self.currentWord = 0
		self.nbLine = 0
		self.fontsize = fontsize
		self.font = pygame.font.SysFont(None, self.fontsize)

		self.txt = text
		self.splitText = splitText

		self.isInitialized = False

	def initialize(self) -> None:
		if self.splitText and (not self.isInitialized):
			# init all texture
			self.allTexture = []
			if self.splitText:
				for i in range(len(self.txt)):
					self.allTexture.append(self.font.render(self.txt[i], True, WHITE))
			
			self.isInitialized = True

	def setText(self, text:str) -> None:
		self.txt = text

	def getTexture(self, time:float) -> None:
		if (self.splitText):

			if time%5 == 0 and self.currentWord < len(self.txt):
				self.currentWord = self.currentWord + 1
				
			if ((self.currentWord * self.fontsize)%600 == 0) and self.nbLine < 3:
				self.nbLine = self.nbLine + 1
			elif self.nbLine == 3:
				self.nbLine = 0

			x = (self.currentWord * (self.fontsize/2))%600
			y = self.nbLine*(self.fontsize + 5)

			print(self.nbLine)

			return (x, y, self.allTexture[self.currentWord])
		else:
			return (0, 0, self.font.render(self.txt, True, WHITE))