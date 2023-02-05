import pygame
from pygame.locals import *

from sceneTools import SceneTools
from textManager import TextManager


class Scene_test_1_1:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/back3_placeholder.jpg",
            [
                "La mauvaise fin...",
                "...",
            ],
            [],
        )

    def update(self):
        self.sceneTools.update()


class Scene_test_1_2:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/back2_placeholder.jpg",
            [
                "La bonne fin !",
                "...",
            ],
            [],
        )

    def update(self):
        self.sceneTools.update() 


class Scene_test:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/background_placeholder.jpg",
            [
                "Bonjour étrangé. Comment ça va vous allez bien ? Moi non j'ai besoin d'être réparé. Je suis vraiment blessé au plus profond de mon être, apporté moi de l'aide je vous en pris. Je ne suis qu'une pauvre petite box... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
                "ça foncte un max ici.",
                "oui.",
                "Bonjour étrangé. Comment ça va vous allez bien ? Moi non j'ai besoin d'être réparé. Je suis vraiment blessé au plus profond de mon être, apporté moi de l'aide je vous en pris. Je ne suis qu'une pauvre petite box... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            ],
            [
                Scene_test_1_1(window, controls), # la scene 1
                Scene_test_1_2(window, controls), # la scene 2
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.eventManagement()

    def eventManagement(self):
        if self.sceneTools.controls.buttonRight:
            self.sceneTools.scene_id_transition = 1 # on change de scène vers la scène 1 avec clique droit
        if self.sceneTools.controls.buttonLeft:
            self.sceneTools.scene_id_transition = 2 # on change de scène vers la scène 2 avec clique droit
