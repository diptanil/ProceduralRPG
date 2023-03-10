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
        self.boxSelectorPos = XYPos(10, 10)

        if self.debug:
            print("Debug Controller")

    def Update(self, screen) -> bool:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self.do_shortcuts(event)

                cameraInput = self.do_cameraInput(event)
                if cameraInput != XYPos(0, 0):
                    self.boxSelectorPos = self.updateSelectorPos(cameraInput)
            if event.type == QUIT:
                return False
        # keys_pressed = pygame.key.get_pressed()
        # cameraInput = self.do_cameraInput(keys_pressed)
        # if cameraInput != XYPos(0, 0):
        #     self.boxSelectorPos = self.updateSelectorPos(cameraInput)
            
        self.sceneManager.Update(screen, boxSelectorPos=self.boxSelectorPos)
        pygame.display.flip()
        return True

    def updateSelectorPos(self, cameraInput):
        __x = self.boxSelectorPos.x + cameraInput.x
        __x = max(0, __x)
        __x = min(__x, GRID_WIDTH - 1)
        
        __y = self.boxSelectorPos.y + cameraInput.y
        __y = max(0, __y)
        __y = min(__y, GRID_HEIGHT - 1)

        return XYPos(__x, __y)

    
    def do_shortcuts(self, event):
        k = event.key
        m = event.mod
        if (k,m) in SHORTCUTS:
            controllerFunc = getattr(self, SHORTCUTS[k,m])
            controllerFunc(self)

    # def do_cameraInput(self, keys_pressed):
    #     __x = 0
    #     __y = 0
    #     if keys_pressed[pygame.K_w]:
    #         __y = -1
    #     if keys_pressed[pygame.K_s]:
    #         __y = 1
    #     if keys_pressed[pygame.K_d]:
    #         __x = 1
    #     if keys_pressed[pygame.K_a]:
    #         __x = -1

    #     return XYPos(__x, __y)

    def do_cameraInput(self, event):
        __x = 0
        __y = 0
        if event.key ==  pygame.K_w:
            __y = -1
        if event.key ==  pygame.K_s:
            __y = 1
        if event.key ==  pygame.K_d:
            __x = 1
        if event.key ==  pygame.K_a:
            __x = -1

        return XYPos(__x, __y)

    def toggle_fullscreen(self):
        self.app.flags ^= pygame.FULLSCREEN
        pygame.display.set_mode((0,0), self.app.flags)

