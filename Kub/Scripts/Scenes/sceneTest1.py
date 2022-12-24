import pygame
from .baseScene import BaseScene

from ..Lookups.lookups import *
from ..Core.proceduralWorldGenerator import ProceduralWorldGenerator
from ..Sprites.spritesManager import SpritesManager

class Scene_Test1(BaseScene):
    _GridPosition = XYPos(20,20)
    
    def __init__(self):
        super().__init__()
        self.terrain = ProceduralWorldGenerator(seed = 2)
        self.spriteManager = SpritesManager()
        
    def Update(self):
        pass

    def textureRule(self, val):
        val = int(val * 100)
        terrainTextures = self.spriteManager.terrainTextures
        sprite = None
        if val < -30:
            sprite = "deep-water"
        elif val >=-30 and val < -20 :
            sprite = "water"
        elif val >=-20 and val < -10 :
            sprite = "shallow-water"
        elif val >=-10 and val < 0 :
            sprite = "wet-sand"
        elif val >= 0 and val < 5 :
            sprite = "sand"
        elif val >=5 and val < 10 :
            sprite = "ground-dirt1"
        elif val >=10 and val < 20 :
            sprite = "grass-light"
        elif val >=20 and val < 40 :
            sprite = "grass-dark"
        elif val >=40 and val < 45 :
            sprite = "rock"
        elif val >= 45:
            sprite = "snow"
        if sprite != None:
            return terrainTextures[sprite]
        return None

    def Render(self, screen):
        screen.fill(COLOR_BACKGROUND)
        self.terrain.drawGrid(screen, Scene_Test1._GridPosition, textureLogic = self.textureRule)