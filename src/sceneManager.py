import pygame
from pygame.locals import *

from textManager import TextManager

class SceneManagement:
    def __init__(self, window, dialogs:list[str], background:str):
        self.dialogs = dialogs
        self.window = window
        self.current_event = None

        # background + dialog
        self.pos_background = [10,10]
        self.pos_dialogs = [10,500]
        self.background = pygame.transform.scale(
            pygame.image.load(background).convert(),
            (800-200,400)
        )
        self.current_dialog = TextManager("Bonjour étrangé.", True) 

        # const

    def update(self) -> None:
        self.eventManager()
        self.current_dialog.initialize()
        self.draw()

    def draw(self) -> None:
        self.drawBackground()
        self.drawDialog()

    def drawBackground(self):
        self.window.blit(self.background, (
            self.pos_background[0], 
            self.pos_background[1]
        ))

    def drawDialog(self):
        text = self.current_dialog
        self.window.blit(text.getTexture(pygame.time.get_ticks()), (
            self.pos_dialogs[0], 
            self.pos_dialogs[1]
        ))

    def eventManager(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.KEYDOWN:
                    self.current_event = event.key
                case pygame.MOUSEBUTTONDOWN:
                    self.current_event = event.button