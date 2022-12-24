import pygame
import random

from .baseScene import BaseScene

from ..Lookups.lookups import *
from ..Core.proceduralWorldGenerator import ProceduralWorldGenerator
from ..Sprites.spritesManager import SpritesManager
from ..UI.text import Text

class Scene_Test1(BaseScene):
    _GridPosition = XYPos(20,20)
    
    def __init__(self):
        super().__init__()
        self.terrain = ProceduralWorldGenerator(seed = 2).noiseGrid
        self.vegetation = self.GenVegetation()
        self.spriteManager = SpritesManager()

        self.spriteManager.boxSelectAnim.iter()
        
    def Update(self):
        pass

    def GenVegetation(self):
        '''
        Only Trees.png considered.
        Trees.png only grow in region grass-dark
        overall cell has 0.75 of having a tree
        CoconutTrees.png only grow in region sand
        overall cell has 0.5 of having a tree
        '''
        overall_treeProb = 0.75
        overall_cocotreeProb = 0.5
        vegetation = [[0 for i in range(GRID_WIDTH)] 
            for j in range(GRID_HEIGHT)]

        random.seed(2)

        for _x in range(GRID_WIDTH):
            for _y in range(GRID_HEIGHT):
                val = int(self.terrain[_y][_x] * 100)
                '''
                Conditions for Tree.png
                Range 1 - 4
                '''
                if val >= 20 and val < 40:
                    isTree = random.random() < overall_treeProb
                    if isTree:
                        vegetation[_x][_y] = random.randint(1, 4)
                
                '''
                Conditions for CoconutTree.png
                Range 5 - 10
                '''
                if val >= 0 and val < 5:
                    isTree = random.random() < overall_cocotreeProb
                    if isTree:
                        vegetation[_x][_y] = random.randint(5, 10)
        
        return vegetation



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

    def vegetationRule(self, val):
        vegetationTextures = self.spriteManager.vegetationTextures
        sprite = None
        if val == 1:
            sprite = "tree-trunk"
        elif val == 2:
            sprite = "tree-bel"
        elif val == 3:
            sprite = "tree-ashoka"
        elif val == 4:
            sprite = "tree-mango"

        elif val == 5:
            sprite = "cocotree-right-trunk"
        elif val == 6:
            sprite = "cocotree-left-trunk"
        elif val == 7:
            sprite = "cocotree-right"
        elif val == 8:
            sprite = "cocotree-right-fruit"
        elif val == 9:
            sprite = "cocotree-left"
        elif val == 10:
            sprite = "cocotree-left-fruit"
        
        if sprite != None:
            return vegetationTextures[sprite]
        return None

    '''
    renderCell function decides which sprites should be rendered
    in each grid cell
    '''
    def renderCell(self, pos: XYPos, screen, cellVal, vegVal):
        '''
        Render order (top - rendered first, bottom rendered last)
        '''
        ############ TERRAIN #############
        terrainSprite = self.textureRule(cellVal)

        if terrainSprite != None:
            screen.blit(terrainSprite, (pos.x, pos.y))
        else:
            rect = pygame.Rect(pos.x, pos.y, SPRITE_SIZE, SPRITE_SIZE)
            img, rectText = Text(str(int(cellVal * 10)), pos=(pos.x + 2, pos.y +2)).render()
            pygame.draw.rect(screen, COLOR_BLACK, rect, 1)
            screen.blit(img, rectText)
        
        ############ VEGETATION #############

        vegetationSprite = self.vegetationRule(vegVal)

        if vegetationSprite != None:
            screen.blit(vegetationSprite, (pos.x, pos.y))
        # else:
        #     rect = pygame.Rect(pos.x, pos.y, SPRITE_SIZE, SPRITE_SIZE)
        #     img, rectText = Text(str(vegVal), pos=(pos.x + 2, pos.y +2)).render()
        #     pygame.draw.rect(screen, COLOR_BLACK, rect, 1)
        #     screen.blit(img, rectText)

            
        
    def renderBoxSelector(self, pos: XYPos, screen):
        screen.blit(self.spriteManager.boxSelectAnim.next(), (pos.x, pos.y))             


    def Render(self, screen, boxSelectorPos: XYPos = XYPos(0, 0), gridViewStart: XYPos = XYPos(0, 0)):
        screen.fill(COLOR_BACKGROUND)

        x_start = max(0, gridViewStart.x)
        y_start = max(0, gridViewStart.y)
        for _x in range(x_start, min(gridViewStart.x + VIEW_WIDTH, GRID_WIDTH)):
            for _y in range(y_start, min(gridViewStart.y + VIEW_HEIGHT, GRID_HEIGHT)):
                x = ((_x - x_start) * SPRITE_SIZE) + Scene_Test1._GridPosition.x
                y = ((_y - y_start) * SPRITE_SIZE) + Scene_Test1._GridPosition.y
                '''
                For each cell in the grid the function renderCell is called
                '''
                self.renderCell(XYPos(x, y), screen, self.terrain[_y][_x], self.vegetation[_x][_y])

                if XYPos(_x, _y) == boxSelectorPos:
                    self.renderBoxSelector(XYPos(x, y), screen)