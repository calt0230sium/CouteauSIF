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
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False

            match self.controls.action():
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
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
            pass

class Scene_chat_2:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous agitez le pointeur laser sur le canapé. Le chat perd soudainement tout intérêt pour vous et semble fasciné par le point rouge. Il saute du buffet, se rue en direction des fauteuils et commence à griffer le cuir frénétiquement là où se trouve le pointeur. Oups. Enfin bon, vous n'êtes pas là pour réparer les canapés de toute façon. Vous reviendrez un autre jour s'il le faut. """.split("\n"),
            [
                Scene_box(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
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
                Scene_box(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


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
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
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
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
            pass

class Scene_chat_6:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous actionnez votre briquet et agitez lentement la flamme devant les yeux du chat. Celui-ci semble perplexe devant la manoeuvre, lève la patte de façon hésitante avant de reculer pour se cacher sous le meuble de la télévision. Parfait.""".split("\n"),
            [
                Scene_box(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False










class Scene_dame:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            [
            "Vous retrouvez Mme. Placeholder devant la porte de sa maison. C'est un ravissant petit pavillon dans un quartier résidentiel de Parici dôté d'un grand jardin. Deux chats flânent dans un arbre et un autre s'étire devant le massif de fleurs.",
            "La propriétaire des lieux vous salue et vous répondez avec le slogan de Répartou™, l'entreprise qui répare tout ! ",
            """ "Ah oui. Parfait. C'est ce qu'il me fallait. Vous êtes là pour mon problème." """,
            lambda : "Euh oui sûrement. Vous n'êtes plus trop sûr de pourquoi vous êtes là d'ailleurs. Bah, vous improviserez." if notlisten else "Ouais ouais réparation de box, vous connaissez. Clairement pas la tâche la plus palpitante mais c'est toujours plus simple que de devoir réparer une relation. Enfin, ce n'est pas comme si vous pouviez choisir vos missions.",
            """"Venez, suivez-moi. Je vais vous montrer où se trouve la box Internet." """
            ],
            [
                Scene_dame_1(window, controls), # la scene 1
                Scene_dame_2(window, controls), # la scene 2
                Scene_dame_3(window, controls), # la scene 2
                Scene_dame_4(window, controls), # la scene 2
                Scene_dame_5(window, controls), # la scene 2
                Scene_dame_6(window, controls), # la scene 2
                Scene_chat(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False

            match self.controls.action():
                case "none":
                    self.sceneTools.scene_id_transition = 7
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

class Scene_dame_1:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous "réparez" de façon définitive tous les problèmes de Mme Placeholder avec votre couteau. Encore une mission réussie ! 
L'air de rien vous retournez à votre camionette pour attendre le prochain appel du patron. Votre travail est si simple !
ENDING COUTEAU Appuyez sur R pour relancer le jeu ou Q pour quitter.""".split("\n"),
            [
            ],
        )
        self.isEnd = True

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
            pass

class Scene_dame_2:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous dégainez votre pointeur laser avec enthousiasme et l'agitez devant les yeux de Mme Placeholder.
"Oui. D'accord. Bon. Monsieur. Monsieur !"
Non attendez, ça ne fait pas partie du protocole standard Répartour™ de rencontre de client. Vous vous calmez.
"Monsieur. Merci. Très bien. Je vais vous emmener à ma box. Suivez-moi. Et ne refaites pas ça !" """.split("\n"),
            [
                Scene_chat(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_dame_3:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """"TUUUUUIIIIIIIIIIIIIIIIT !!" 
Mme Placeholder devient toute rouge devant la joie que vous semblez prendre à souffler dans votre sifflet. 
"Non. Stop. Monsieur. Arrêtez monsieur. Monsieur !"
Vous décidez, à grand peine d'arrêter. 
"Oui. C'est mieux. Arrêtons ces bêtises. Suivez-moi, je vais vous montrer où se trouve ma box Internet." """.split("\n"),
            [
                Scene_chat(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_dame_4:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous montrez la lame-tournevis de votre couteau suisse à Mme. Placeholder.
"Ah oui ! Je vois bien que vous êtes là pour réparer de choses. Vous êtes très équipé. Bravo."
Elle ne se doute de rien quand à l'état de votre équipement, parfait. Si tous les clients d'aujourd'hui (et leurs problèmes) sont aussi facile à gérer, vous allez peut-être vous en sortir.
"Vous avez l'air très prêt. Suivez-moi je vais vous montrer ma box Internet." """.split("\n"),
            [
                Scene_chat(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_dame_5:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous poussez légèrement Mme Placeholder de l'épaule pour essayer la clé de votre couteau suisse dans la serrure de sa maison. De façon peu surprenante, ce ne semble pas âtre la clé de la maison de Mme Placeholder. Vous forcez légèrement (au cas où), ce qui n'a pas d'effet. 
"Monsieur. Que faites-vous. La porte est déjà ouverte, arrêtez monsieur."
Vous rangez votre clé l'air tout penaud. 
"Suivez-moi puisque vous tenez à rentrer. Venez. Je vais vous montrer ma box qui ne marche pas." """.split("\n"),
            [
                Scene_chat(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_dame_6:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous décidez que le moment est bien choisi pour essayer votre nouveau briquet. Après quelques essais infructueux, vous prenez le coup de main et produisez un belle flamme.
Mme. Placeholder semble ignorer votre petit jeu et vous fait signe de rentrer :
"Allons donc à l'intérieur. Je vais vous montrer ma Box Internet." """.split("\n"),
            [
                Scene_chat(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False






class Scene_box:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous avez maintenant accès à la box Internet ! Celle-ci trône sur petit napperon vert couvert de poils de chat, posé sur un gros buffet en bois massif.
La box semble inactive. Même si vous êtes censé la réparer, vos connaissances dans le domaine spécifique des routeurs sont limitées. Mais normalement il devrait y avoir des lumières qui clignotent ou un truc dans le genre. Vous cherchez un manuel du regard autour de vous sans succès. Peut-être se trouve-t'il dans un placard du buffet ? Les portes sont fermées à clé.
Votre attention est attirée par un petit boitier à vis à sur le côté de l'appareil. Il est possible que vous puissiez trouver un moyen de redémarrer la Box à l'intérieur.
Que faites-vous ?""".split("\n"),
            [
                Scene_box_1(window, controls), # la scene 1
                Scene_box_2(window, controls), # la scene 2
                Scene_box_3(window, controls), # la scene 2
                Scene_box_4(window, controls), # la scene 2
                Scene_box_5(window, controls), # la scene 2
                Scene_box_6(window, controls) # la scene 2
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False

            match self.controls.action():
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

class Scene_box_1:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous faites sauter l'opercule du petit boitier avec votre couteau. Pas dit que vous puissiez le remettre en place mais si ça vous permet de réparer le routeur...
L'intérieur est rempli de fils et de diodes en tou genres auxquels vous ne comprenez pas grand chose. Vous prenez la Box dans vos mains pour y voir de plus clair et réalisez qu'elle n'est en fait pas branchée. 
Vous trouvez une prise et alimentez l'appareil. Il commence à clignoter. Bon travail, c'est réparé !
Vous annoncez à Mme. Placeholder que vous avez réparé sa Box avant de retourner à votre camionette.
Plus qu'à attendre la prochaine mission. C'était facile !
GOOD ENDING""".split("\n"),
            [
            ],
        )
        self.isEnd = True

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
            pass

class Scene_box_2:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous flashez votre laser sur la box qui ne réagit pas. Comme c'est inattendu.""".split("\n"),
            [
                # Scene_box(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_box_3:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """"TUUUUUIIIIIIIIIIIIIIIIT !!" 
Votre enthousiasme est communicatif et la Box Internet vous répond :
"TUUUUUIIIIIIIIIIIIIIIIT !!
-TUUIIIIIUUUIIIIIIIIIIIT !!
-TUIUIUIIIIIIIIIIIIIIIIT !!" 
OK. Vous n'êtes pas trop sûr de pourquoi ça a marché mais elle a l'air d'être allumée maintenant. Bon travail.
Vous annoncez à Mme. Placeholder que vous avez réparé sa Box avant de retourner à votre camionette.
Plus qu'à attendre la prochaine mission. C'était facile !
GOOD ENDING""".split("\n"),
            [
            ],
        )
        self.isEnd = True

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
            pass

class Scene_box_4:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous dévissez l'opercule du boitier avec minutie. Les vis sont très serrées et vous devez forcer. La dernière vis brise la tête de votre tournevis mais heureusement vous parvenez à déloger le boitier.
L'intérieur est rempli de fils et de diodes en tou genres auxquels vous ne comprenez pas grand chose. Vous prenez la Box dans vos mains pour y voir de plus clair et réalisez qu'elle n'est en fait pas branchée. 
Vous trouvez une prise et alimentez l'appareil. Il commence à clignoter. Bon travail, c'est réparé !""".split("\n"),
            [
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
            pass

class Scene_box_5:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous insérez la clé dans la serrure d'un des placards du buffet avec succès. A l'intérieur, pas de manuel de routeur mais un slot d'inventaire supplémentaire !""".split("\n"),
            [
                Scene_box(window, controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_box_6:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous mettez le feu à la Box Internet dans le doute. Celle-ci est maintenant allumée (littéralement).
Ouais euh. Ça n'était peut-être pas une idée si brillante. Un odeur de plastique brûlé commence à flotter dans la maison et attire Mme. Placeholder au rez-de-chaussée.
"Mais ?! Qu'avez-vous fait ? Ma box est en train de brûler ?? Vilain monsieur ! Pyromane ! Sortez de chez moi !"
Vous ne vous faites pas prier pour retourner à votre camionette. Honnêtement vous n'êtes pas trop sûr de ce qui vous est passé par la tête.
**BAD ENDING** Vous n'avez pas pu réparer la Box. Appuyez sur R pour relancer le jeu ou Q pour quitter.""".split("\n"),
            [
            ],
        )
        self.isEnd = True

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False
            pass






        

class Scene_camion2:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Soudain, le téléphone de la camionette sonne ! C'est votre patron qui vous appelle pour vous diriger vers votre premier client de la journée.
"Allo. C'est toi ? Prêt à démarrer ?"
Vous omettez de mentionner l'oubli de votre trousse à outils. Le patron n'a pas vraiment besoin de le savoir. 
"OK alors on est partis ! Ta première tâche de la journée est de réparer une box Internet. Je sais que tu es habitué à des réparations plus compliquées mais on commence doucement hein ? OK. Notre cliente est une certaine madame Placeholder. Elle ne vit pas très loin du bureau, sa maison se trouve au 5 rue de la Jam, à Parici-en-Trédonc. Fais ça vite d'accord, je te veux disponible pour la tâche suivante. Je suis sûr que ce sera une grosse journée."
Vous acquiesez et démarrez la camionette. En route pour votre destination. """.split("\n"),
            [
                Scene_camion2_1(window, controls), # la scene 1
                Scene_camion2_2(window, controls), # la scene 2
                Scene_camion2_3(window, controls), # la scene 2
                Scene_camion2_4(window, controls), # la scene 2
                Scene_camion2_5(window, controls), # la scene 2
                Scene_dame(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False

            match self.controls.action():
                case "none":
                    self.sceneTools.scene_id_transition = 6
                case "couteau":
                    self.sceneTools.scene_id_transition = 1
                case "laser":
                    notlisten = True
                    self.sceneTools.scene_id_transition = 2
                case "sifflet":
                    self.sceneTools.scene_id_transition = 3
                case "tournevis":
                    self.sceneTools.scene_id_transition = 4
                case "cle":
                    self.sceneTools.scene_id_transition = 5
                case "briquet":
                    pass

class Scene_camion2_1:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous coupez le fil du combiné. Oh non ! Vous l'avez encore fait...
Heureusement, vous embarquez toujours plusieurs fils de téléphone à l'arrière de la camionette. Une sage précaution au vu de votre tendance à les trancher.
Vous trouvez aussi un slot d'inventaire supplémentaire ! **OBTENU** Slot d'inventaire supplémentaire !
Après un peu de bricolage, le téléphone est comme neuf. Vous composez le numéro du bureau et votre patron décroche :
"Ça t'est encore arrivé hm ? Bon allez. Ta première mission du jour est d'aller réparer la Box Internet de Mme Placeholder au 5 rue de la Jam, à Parici-en-Trédonc. je raccroche avant que tu coupes de nouveau."
Vous vous mettez en route...""".split("\n"),
            [
                Scene_dame(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_camion2_2:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Blablabla, le patron parle, pewpew, le pointeur laser danse sur tableau de bord. 
Au moment où vous réalisez que vous auriez peut-être dû écouter les instructions au lieu de jouer avec votre couteau suisse, vous avez à peine le temps d'attraper votre destination au vol avant que le patron raccroche.
(si pile vide) Votre session de jeu est interrompue par la pile de pointeur qui tombe à plat de toute façon. Vous aviez des 
Bon eh bien en route.""".split("\n"),
            [
                Scene_dame(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_camion2_3:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """"TUUUUUUUIIIIIIIIIIIIIIIIT !!" Vous sifflez de toutes vos forces dans le combiné. Vous pouvez entendre des injures de l'autre côté du fil.
Après quelques instants, votre patron reprend :
"C'est bon, tu as fini ? Tu t'es lâché ? Allez hop au travail. Ta première mission du jour est d'aller réparer la Box Internet de Mme Placeholder au 5 rue de la Jam, à Parici-en-Trédonc."
Il raccroche brusquement. Bon eh bien plus qu'à se mettre en route.""".split("\n"),
            [
                Scene_dame(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_camion2_4:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous coincez le combiné contre votre épaule et cherchez un truc à faire avec votre tournevis pendant que le patron parle. Vous remarquez un compartement vissé sur le tableau de bord et entreprenez de l'ouvrir. 
Alors que vous dévissez la dernière vis, votre lame se coince. En forçant un peu vous parvenez à déloger le compartiment mais votre tournevis casse !
A l'intérieur, vous trouvez une lame briquet. Vous profitez de l'occasion pour remplacer la lame tournevis cassée de votre couteau suisse.
Pendant l'opération, vous écoutez distraitement le patron vous expliquer que vous devez réparer un box Internet à Parici-en-Trédonc. Le temps de monter votre nouvelle lame, vous démarrez la camionette et vous mettez en route.""".split("\n"),
            [
                Scene_dame(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_camion2_5:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            """Vous observez longuement la clé de votre couteau suisse. Vous essayez de vous rappeler ce qu'elle ouvre. Le patron dit des mots dans le combiné que vous n'écoutez qu'à moitié, suffisamment pour retenir que vous devez réparer une box à Parici-en-Trédonc.
D'où vient cette clé déjà ? Elle était déjà sur le couteau suisse quand vous l'avez obtenu. Vous ne vous souvenez plus trop d'où vient le couteau suisse d'ailleurs. C'est quand même sacrément pratique que vous l'ayez gardé depuis tout ce temps.
Perdu dans vos pensées, vous vous dirigez vers la localisation de votre mission.""".split("\n"),
            [
                Scene_dame(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False



class Scene_camion1:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            [
                "Le moteur de la camionette ronronne doucement. Une autre journée qui commence.",
                "Vous êtes technicien chez Répartou™, l'entreprise qui répare tout ! (ou tout du moins, c'est le slogan que vous êtes légalement tenu de clamer à tous les clients).",
                "Tous les jours, au volant de votre camionette, vous êtes sur la route pour réparer les problèmes variés des clients chez qui votre patron vous envoie.",
                "Mais aujourd'hui il y a un problème : vous avez oublié votre *trousse à outils* ce matin. Difficile de réparer quoi que ce soit sans...",
                "Vous avez cependant, comme toujours, votre fidèle *couteau suisse* ! ",
                "Avec un peu de chance vous pourrez accomplir toutes les tâches d'aujourd'hui simplement avec votre couteau suisse."
            ],
            [
                Scene_camion1_1(window, controls), # la scene 1
                Scene_camion1_2(window, controls), # la scene 2
                Scene_camion1_3(window, controls), # la scene 2
                Scene_camion1_4(window, controls), # la scene 2
                Scene_camion1_5(window, controls), # la scene 2
                Scene_camion2(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False

            match self.controls.action():
                case "none":
                    self.sceneTools.scene_id_transition = 6
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
                    pass
                    

class Scene_camion1_1:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            [
                "Vous agitez votre couteau devant vous en vue d'une confrontation imaginaire. Un passant sur le trottoir d'en face est vaguement mal à l'aise."
            ],
            [
                Scene_camion2(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_camion1_2:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            [
                "Vous agitez distraitement le pointeur laser au plafond de la camionette."
            ],
            [
                Scene_camion2(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_camion1_3:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            [
                "'TUUUUUUUUIIIIIIIIIIIIIIIIT !!' Personne n'a de temps pour l'exposition scénaristique."
            ],
            [
                Scene_camion2(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_camion1_4:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            [
                "Vous observez la lame tournevis d'un air satisfait. Avec un tournevis, qu'est-ce qui pourrait mal se passer ?"
            ],
            [
                Scene_camion2(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


class Scene_camion1_5:
    def __init__(self, window, controls):
        self.sceneTools = SceneTools(
            window,
            controls,
            "../assets/camionette1.png",
            [
                "C'est une clé. Vous ne savez pas trop pourquoi il y a une lame clé sur le couteau suisse ni même ce qu'elle ouvre mais vous n'avez jamais osé l'enlever."
            ],
            [
                Scene_camion2(window,controls)
            ],
        )

    def update(self):
        self.sceneTools.update()
        self.sceneTransition()

    def sceneTransition(self):
        if self.controls.isActionTriggered():
            self.controls.actionTrigger = False


