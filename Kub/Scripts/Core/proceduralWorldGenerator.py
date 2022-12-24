import pygame

from ..UI.text import Text
from ..Lookups.lookups import *
from perlin_noise import PerlinNoise

class ProceduralWorldGenerator:
    def __init__(self, octaves = 4, seed = 2):
        print("Running procedural world generator")

        '''
        Setting up Perlin noise using the parameters
        octaves - 
        seed - 
        '''
        self.noise = PerlinNoise(octaves=octaves, seed=seed)
        self.noiseGridGenerator()


    '''
    Generating a noise grid of GRID_WIDTH x GRID_HEIGHT
    using Perlin noise
    '''
    def noiseGridGenerator(self):
        self.noiseGrid = [[self.noise([i/GRID_WIDTH, 
        j/GRID_HEIGHT]) for i in range(GRID_WIDTH)] 
        for j in range(GRID_HEIGHT)]

    def drawGrid(self, screen, pos: XYPos = XYPos(0, 0), textureLogic = None):
        for _x in range(GRID_WIDTH):
            for _y in range(GRID_HEIGHT):
                x = (_x * SPRITE_SIZE) + pos.x
                y = (_y * SPRITE_SIZE) + pos.y
                rect = pygame.Rect(x, y, SPRITE_SIZE, SPRITE_SIZE)
                rectValue = self.noiseGrid[_y][_x]

                showVal = True

                # Texture condition
                if textureLogic != None:
                    sprite = textureLogic(rectValue)
                    # screen.blit(sprite, (x, y))
                    if sprite != None:
                        screen.blit(sprite, (x, y))
                        showVal = False

                # If no texture then print the value
                if showVal:
                    img, rectText = Text(str(int(rectValue * 10)), pos=(x + 2, y +2)).render()
                    pygame.draw.rect(screen, COLOR_BLACK, rect, 1)
                    screen.blit(img, rectText)