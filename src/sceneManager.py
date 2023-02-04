import pygame
from pygame.locals import *

from textManager import TextManager

class SceneManagement:
    def __init__(
        self, 
        window,
        controls,
        background:str,
        dialogs:list[str],
    ):
        self.dialogs = dialogs
        self.window = window
        self.controls = controls
        self.current_event = None
        
        # background + dialog
        self.pos_background = [10,10]
        self.pos_dialogs = [10,420]
        self.background = pygame.transform.scale(
            pygame.image.load(background).convert(),
            (800-200,400)
        )
        self.current_dialog = TextManager(dialogs[0], 25, True)
        self.isEnd = False

        # const

    def update(self) -> None:
        print(self.controls.space)
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
        tuple_dialog = text.getTexture(pygame.time.get_ticks())
        self.window.blit(tuple_dialog[2], (
            self.pos_dialogs[0] + tuple_dialog[0], 
            self.pos_dialogs[1] + tuple_dialog[1]
        ))