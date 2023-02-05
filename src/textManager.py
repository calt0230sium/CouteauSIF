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

		self.timer = 0

		self.txt = text
		self.splitText = splitText

		self.isInitialized = False
		self.textEnd = False

	def initialize(self) -> None:
		if self.splitText and (not self.isInitialized):
			# init all texture
			
			self.allTexture = []
			maxWidth = 0
			maxHeight = 0

			saveLine = []
			lower_bound = 0

			if self.splitText:
				for i in range(len(self.txt)):
					currentTexture = self.font.render(self.txt[lower_bound:i+1], True, WHITE)
					endTexture = pygame.Surface((650, 200), pygame.SRCALPHA)

					total_height = 0
					for j, line in enumerate(saveLine):
						total_height = total_height + 20
						endTexture.blit(
							line, 
							(0, total_height)
						)

					if currentTexture.get_width() >= 600 or (self.txt[i:i+1] == ' ' and currentTexture.get_width() >= 550):
						lower_bound = i+1
						saveLine.append(currentTexture)

					endTexture.blit(
						currentTexture, 
						(0, total_height + 20)
					)

					self.allTexture.append(endTexture)
			
			self.isInitialized = True

	def setText(self, text:str) -> None:
		self.txt = text

	def getTexture(self, time:float) -> None:
		if (self.splitText):

			end_timer = 8

			if self.timer < end_timer:
				self.timer = self.timer + 1

			if self.timer == end_timer and self.currentWord < len(self.allTexture) - 1:
				self.timer = 0
				self.currentWord = self.currentWord + 1
			elif self.currentWord == len(self.allTexture) - 1:
				self.textEnd = True

			return self.allTexture[self.currentWord]
		else:
			return self.font.render(self.txt, True, WHITE)