import pygame
from pygame.locals import *

from sceneManager import SceneManagement
from textManager import TextManager

def hello():
    print("hello")


class Scene_test:
    def __init__(self, window, controls):
        self.sceneTools = SceneManagement(
            window,
            controls,
            "../assets/background_placeholder.jpg" 
        )

    def update(self):
        # self.eventManager()
        self.sceneTools.update()