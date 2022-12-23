import pygame
from pygame.locals import *

from .UI.text import Text
from .Lookups.shortcuts import Shortcuts
from .Core.controller import Controller
class App:
    "Create a single window app with multiple Scenes"

    def __init__(self):
        pygame.init()

        self.fps = 60

        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 640, 240)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        App.t = Text('Pygame App', pos = (20,20))

        self.controller = Controller()

        self.shortcuts = Shortcuts().shortcuts

        App.running = True

    def run(self):
        """"Run main event loop"""
        clock = pygame.time.Clock()
        while App.running:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.do_shortcuts(event)
                if event.type == QUIT:
                    App.running = False
            App.screen.fill(Color('gray'))
            App.t.draw(self)
            pygame.display.update()

        pygame.quit()

    def do_shortcuts(self, event):
        k = event.key
        m = event.mod
        if (k,m) in self.shortcuts:
            controllerFunc = getattr(self.controller, self.shortcuts[k,m])
            controllerFunc(self)
            # exec(self.controller[k,m])
