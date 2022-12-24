import pygame
from .baseScene import BaseScene

from ..Scripts.Lookups.lookups import *

class Scene_Test1(BaseScene):
    def __init__(self):
        super().__init__()

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.SwitchToScene(None)

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill(COLOR_BACKGROUND)