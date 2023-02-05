import pygame
from pygame.locals import *

from sceneManager import SceneManagement
from textManager import TextManager

class Scene_test:
    def __init__(self, window, controls):
        self.sceneTools = SceneManagement(
            window,
            controls,
            "../assets/background_placeholder.jpg",
            [
                "Bonjour étrangé. Comment ça va vous allez bien ? Moi non j'ai besoin d'être réparé. Je suis vraiment blessé au plus profond de mon être, apporté moi de l'aide je vous en pris. Je ne suis qu'une pauvre petite box... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
                "ça foncte un max ici.",
                "oui.",
                "Bonjour étrangé. Comment ça va vous allez bien ? Moi non j'ai besoin d'être réparé. Je suis vraiment blessé au plus profond de mon être, apporté moi de l'aide je vous en pris. Je ne suis qu'une pauvre petite box... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            ]
        )

    def update(self):
        self.sceneTools.update()