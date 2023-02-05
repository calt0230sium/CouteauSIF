import pygame
from pygame.locals import *

from textManager import TextManager


class SceneTools:
    def __init__(
        self, 
        window,
        controls,
        background:str,
        dialogs:list[str],

        nodes_scenes:None,
    ):
        self.dialogs = dialogs
        self.window = window
        self.controls = controls
        self.scene_id_transition = 0
        self.nodes_scenes = nodes_scenes
        self.current_event = None
        
        # const
        self.size_font = 28

        # background + dialog
        self.pos_background = [10,10]
        self.pos_dialogs = [10,400]
        self.background = pygame.transform.scale(
            pygame.image.load(background).convert(),
            (600,400)
        )
        self.id_dialog = 0
        self.current_dialog = TextManager(self.dialogs[self.id_dialog], self.size_font, True)
        self.isEnd = False

    def update(self) -> None:
        self.dialogTransition()
        self.current_dialog.initialize()
        self.draw()

    def dialogTransition(self) -> None:
        if self.controls.isActionTriggered():
            
            match self.controls.action():
                case "none":
                    if self.current_dialog.textEnd and self.id_dialog < (len(self.dialogs)-1):
                        self.id_dialog = self.id_dialog + 1
                        self.current_dialog = TextManager(self.dialogs[self.id_dialog], self.size_font, True)

            
    def draw(self) -> None:
        self.drawBackground()
        self.drawDialog()

    def drawBackground(self):
        self.window.blit(self.background, (
            self.pos_background[0], 
            self.pos_background[1],
        ))

    def drawDialog(self):
        text = self.current_dialog
        self.window.blit(text.getTexture(pygame.time.get_ticks()), (
            self.pos_dialogs[0], 
            self.pos_dialogs[1],
        ))

    def sceneTransition(self):
        if self.scene_id_transition != 0:
            return self.nodes_scenes[self.scene_id_transition-1]
        else:
            return None