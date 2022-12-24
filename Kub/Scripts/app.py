import pygame
from pygame.locals import *

from .UI.text import Text
from .Lookups.lookups import *
from .Core.controller import Controller
from ..Scenes.sceneTest1 import Scene_Test1

class App:
    "Create a single window app with multiple Scenes"

    def __init__(self):
        pygame.init()

        self.fps = 60

        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 640, 240)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        App.t = Text('Pygame App', pos = (20,20))

        self.startingScene = Scene_Test1()

        self.controller = Controller()

        App.running = True

    def run(self):
        """"Run main event loop"""
        clock = pygame.time.Clock()
        active_scene = self.startingScene
        while App.running:
            clock.tick(self.fps)
            filtered_events = []
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                quit_attempt = False
                if event.type == KEYDOWN:
                    self.do_shortcuts(event)
                if event.type == QUIT:
                    App.running = False
                if quit_attempt:
                    active_scene.Terminate()
                else:
                    filtered_events.append(event)
                
            active_scene.ProcessInput(filtered_events, pressed_keys)
            active_scene.Update()
            active_scene.Render(App.screen)

            active_scene = active_scene.next
            # App.screen.fill(Color('gray'))
            # App.t.draw(self)
            pygame.display.flip()

        pygame.quit()

    def do_shortcuts(self, event):
        k = event.key
        m = event.mod
        if (k,m) in SHORTCUTS:
            controllerFunc = getattr(self.controller, SHORTCUTS[k,m])
            controllerFunc(self)
            # exec(self.controller[k,m])
