import pygame
from pygame.locals import *

from ..Lookups.lookups import *
from ..Scenes.sceneManager import SceneManager
from ..Utils.utils import *

class Controller:
    def __init__(self, app, debug = False):
        self.app = app
        self.debug = debug

        self.sceneManager = SceneManager()

        '''
        This variable keeps track of the top-left
        cell value of the visivle grid
        '''
        self.gridViewStart = XYPos(0, 0)

        if self.debug:
            print("Debug Controller")

    def Update(self, screen) -> bool:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self.do_shortcuts(event)
                cameraInput = self.do_cameraInput(event)
                if cameraInput != XYPos(0, 0):
                    # print("XXX")
                    self.gridViewStart = self.updateGridView(cameraInput)
                # print(self.gridViewStart.x, self.gridViewStart.y)
            if event.type == QUIT:
                return False
            
        self.sceneManager.Update(screen, gridViewStart=self.gridViewStart)
        pygame.display.flip()
        return True

    def updateGridView(self, cameraInput):
        # print(f"{self.gridViewStart.x}, {cameraInput.x}")
        __x = self.gridViewStart.x + cameraInput.x
        __x = max(0, __x)
        __x = min(__x, GRID_WIDTH - VIEW_WIDTH)
        
        __y = self.gridViewStart.y + cameraInput.y
        __y = max(0, __y)
        __y = min(__y, GRID_WIDTH - VIEW_WIDTH)

        return XYPos(__x, __y)

    
    def do_shortcuts(self, event):
        k = event.key
        m = event.mod
        if (k,m) in SHORTCUTS:
            controllerFunc = getattr(self, SHORTCUTS[k,m])
            controllerFunc(self)

    def do_cameraInput(self, event):
        __x = 0
        __y = 0
        if event.key == pygame.K_w:
            __y = -1
        if event.key == pygame.K_s:
            __y = 1
        if event.key == pygame.K_d:
            __x = 1
        if event.key == pygame.K_a:
            __x = -1

        return XYPos(__x, __y)

    def toggle_fullscreen(self):
        self.app.flags ^= pygame.FULLSCREEN
        pygame.display.set_mode((0,0), self.app.flags)

