import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255,255,255)

class TextManager:
	def __init__(self, text:str) -> None:
		self.txt = text
		self.font = pygame.font.SysFont(None, 48)

	def setText(self, text:str) -> None:
		self.txt = text

	def getTexture(self) -> pygame.Surface:
		return self.font.render(self.txt, True, WHITE)