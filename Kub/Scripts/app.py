import pygame
from pygame.locals import *

from .Lookups.lookups import *
from .Core.controller import Controller
from .Scenes.sceneManager import SceneManager

class App:
    "Create a single window app with multiple Scenes"

    def __init__(self):
        pygame.init()

        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 600, 600)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)

        self.sceneManager = SceneManager()

        self.controller = Controller()

        App.running = True

    def run(self):
        """"Run main event loop"""
        clock = pygame.time.Clock()
        while App.running:
            clock.tick(FPS)
            for event in pygame.event.get():
                quit_attempt = False
                if event.type == KEYDOWN:
                    self.do_shortcuts(event)
                if event.type == QUIT:
                    App.running = False
                if quit_attempt:
                    self.sceneManager.Terminate()
                
            self.sceneManager.Update(App.screen)
            pygame.display.flip()

        pygame.quit()

    def do_shortcuts(self, event):
        k = event.key
        m = event.mod
        if (k,m) in SHORTCUTS:
            controllerFunc = getattr(self.controller, SHORTCUTS[k,m])
            controllerFunc(self)
