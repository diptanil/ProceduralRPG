from .sceneTest1 import Scene_Test1
from ..Utils.utils import *


class SceneManager:
    def __init__(self):
        self.startingScene = Scene_Test1()
        self.activeScene = self.startingScene

    def Update(self, screen, boxSelectorPos:XYPos = XYPos(0, 0), new_scene = None, gridViewStart = XYPos(0, 0)):
        self.activeScene.Update()
        self.activeScene.Render(screen, boxSelectorPos=boxSelectorPos, gridViewStart=gridViewStart)
        if new_scene != None:
            self.activeScene.SwitchToScene(new_scene)
        
        self.activeScene = self.activeScene.next
    
    def Terminate(self):
        self.activeScene.Terminate()