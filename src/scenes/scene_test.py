from sceneManager import SceneManagement

def hello():
    print("hello")


class Scene_test:
    def __init__(self, window):
        self.sceneTools = SceneManagement(
            window, 
            [], 
            "../assets/background_placeholder.jpg"
        )

    def update(self):
        self.interaction()
        self.sceneTools.update()
    
    def interaction(self):
        match self.sceneTools.current_event:
            case _:
                pass