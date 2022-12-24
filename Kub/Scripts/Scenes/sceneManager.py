from .sceneTest1 import Scene_Test1

class SceneManager:
    def __init__(self):
        self.startingScene = Scene_Test1()
        self.activeScene = self.startingScene

    def Update(self, screen, new_scene = None):
        self.activeScene.Update()
        self.activeScene.Render(screen)
        if new_scene != None:
            self.activeScene.SwitchToScene(new_scene)
        
        self.activeScene = self.activeScene.next
    
    def Terminate(self):
        self.activeScene.Terminate()