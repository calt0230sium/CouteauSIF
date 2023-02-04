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
            "../assets/background_placeholder.jpg",
            [
                "Bonjour étrangé. Comment ça va vous allez bien ? Moi non j'ai besoin d'être réparé. Je suis vraiment blessé au plus profond de mon être, apporté moi de l'aide je vous en pris. Je ne suis qu'une pauvre petite box...",
            ]
        )

    def update(self):
        self.sceneTools.update()