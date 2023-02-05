import pygame
from pygame.locals import *

from sceneTools import SceneTools
from textManager import TextManager

notlisten = False
battery = 2


class Scene_chat:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Mme Placeholder vous guide dans l'entrée et vous pointe le salon. Elle marmonne quelque chose au sujet de devoir aller s'occuper de ses chats puis monte à l'étage.
Vous rentrez dans le salon. Quelques fauteuils en cuir couverts de traces de griffes entourent un vieux téléviseur éteint. Sur la gauche, une table à manger avec une nappe à fleur baigne dans le soleil du matin. Au fond de la pièce se tient un buffet en bois aux placards fermés à clé sur lequel se trouve un appareil dont la modernité jure avec le reste du décor. C'est la Box Internet. Un chat blanc dort sur le routeur.
Lorsque vous vous approchez, celui-ci ouvre un oeil pour jauger la situation, et se lève en constatant que vous venez pour le déranger. Il feule et arque le dos. Que faites-vous ? """.split("\n"),
            [
                Scene_chat_1(window, controls), # la scene 1
                Scene_chat_2(window, controls), # la scene 2
                Scene_chat_3(window, controls), # la scene 2
                Scene_chat_4(window, controls), # la scene 2
                Scene_chat_5(window, controls), # la scene 2
                Scene_chat_6(window, controls) # la scene 2
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.sceneTools.controls.isActionTriggered():
            self.sceneTools.controls.actionTrigger = False

            match self.sceneTools.controls.action():
                case "none":
                    pass
                case "couteau":
                    self.sceneTools.scene_id_transition = 1
                case "laser":
                    self.sceneTools.scene_id_transition = 2
                case "sifflet":
                    self.sceneTools.scene_id_transition = 3
                case "tournevis":
                    self.sceneTools.scene_id_transition = 4
                case "cle":
                    self.sceneTools.scene_id_transition = 5
                case "briquet":
                    self.sceneTools.scene_id_transition = 6

class Scene_chat_1:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous "réparez" de façon définitive le problème du chat à l'aide de votre couteau. 
Mme. Placeholder, qui était redesencdue vous surveiller, rentre dans la pièce dans pas précipité.
"Qu'avez-vous fait à mon chat ?! Vilain homme ! Sortez ! Sortez d'ici !"
Elle attrape un balai qui posé derrière la porte et commence à vous pourchasser avec. Vous décidez de battre en retraite à la camionette. 
**BAD ENDING** Vous n'avez pas pu réparer la Box. Appuyez sur R pour relancer le jeu ou Q pour quitter.""".split("\n"),
            [
            ],
        )
        self.isEnd = True

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.sceneTools.controls.isActionTriggered():
            self.sceneTools.controls.actionTrigger = False
            pass

class Scene_chat_2:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous agitez le pointeur laser sur le canapé. Le chat perd soudainement tout intérêt pour vous et semble fasciné par le point rouge. Il saute du buffet, se rue en direction des fauteuils et commence à griffer le cuir frénétiquement là où se trouve le pointeur. Oups. Enfin bon, vous n'êtes pas là pour réparer les canapés de toute façon. Vous reviendrez un autre jour s'il le faut. """.split("\n"),
            [
                # Scene_box(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.sceneTools.controls.isActionTriggered():
            self.sceneTools.controls.actionTrigger = False
            pass
            

class Scene_chat_3:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """"TUUUUUIIIIIIIIIIIIIIIIT !!" 
Vous agressez l'ouïe du félin à l'aide de votre sifflet. Celui-ci crache dans votre direction, l'air très irrité, avant de prendre la fuite en direction de la porte.
Vous entendez Mme. Placeholder rouspéter à l'étage mais elle ne semble pas redescendre.""".split("\n"),
            [
                # Scene_box(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.sceneTools.controls.isActionTriggered():
            self.sceneTools.controls.actionTrigger = False


class Scene_chat_4:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous présentez votre tournevis au félin pour le convaincre que vous êtes ici dans un but strictement réparateur. Celui-ci n'est pas sensible à vos arguments et vous griffe. Vous faites un bond en arrière.""".split("\n"),
            [
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.sceneTools.controls.isActionTriggered():
            self.sceneTools.controls.actionTrigger = False
            pass

class Scene_chat_5:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous vous avancez pour ouvrir l'un des placards du buffet à l'aide de votre clé mais le chat interprète votre mouvement comme une tentative d'agression et griffe votre main quand vous l'approchez du meuble ! Vous reculez rapidement.
""".split("\n"),
            [
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.sceneTools.controls.isActionTriggered():
            self.sceneTools.controls.actionTrigger = False
            pass

class Scene_chat_6:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous actionnez votre briquet et agitez lentement la flamme devant les yeux du chat. Celui-ci semble perplexe devant la manoeuvre, lève la patte de façon hésitante avant de reculer pour se cacher sous le meuble de la télévision. Parfait.""".split("\n"),
            [
                # Scene_box(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.sceneTools.controls.isActionTriggered():
            self.sceneTools.controls.actionTrigger = False
