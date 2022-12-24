import pygame
from pygame.locals import *

from .Lookups.lookups import *
from .Core.controller import Controller

class App:
    "Create a single window app with multiple Scenes"

    def __init__(self):
        pygame.init()

        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 600, 600)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)

        self.controller = Controller(self)

        App.running = True

    def run(self):
        """"Run main event loop"""
        clock = pygame.time.Clock()
        while App.running:
            clock.tick(FPS)
            App.running = self.controller.Update(App.screen)         

        pygame.quit()

    
