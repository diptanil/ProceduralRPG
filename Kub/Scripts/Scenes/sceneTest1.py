import pygame
from .baseScene import BaseScene

from ..Lookups.lookups import *
from ..Core.proceduralWorldGenerator import ProceduralWorldGenerator

class Scene_Test1(BaseScene):
    _GridPosition = XYPos(20,20)
    
    def __init__(self):
        super().__init__()
        self.terrain = ProceduralWorldGenerator()
        
    def Update(self):
        pass

    def Render(self, screen):
        screen.fill(COLOR_BACKGROUND)
        self.terrain.drawGrid(screen, Scene_Test1._GridPosition)