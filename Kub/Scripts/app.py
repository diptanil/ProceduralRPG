import pygame
from pygame.locals import *

from .UI.text import Text
from .Lookups.shortcuts import Shortcuts
class App:
    "Create a single window app with multiple Scenes"

    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((640, 240), flags)
        App.t = Text('Pygame App', pos = (20,20))

        self.shortcuts = Shortcuts().shortcuts

        App.running = True

    def run(self):
        """"Run main event loop"""
        while App.running:
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
            exec(self.shortcuts[k,m])
