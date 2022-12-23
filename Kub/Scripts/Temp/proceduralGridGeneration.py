import pygame
from pygame.locals import *
import numpy as np
from perlin_noise import PerlinNoise

class Text:
    '''
    Create a text object.
    Variables: 
    '''

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 16
        self.fontcolor = Color('black')
        self.set_font()
        # self.render()

    def set_font(self):
        """Set the font object from //fontname and //fontsize"""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image using //fontcolor"""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        return self.img, self.rect


class ProceduralGridGeneration:
    ''' 
    Procedurally generates a world
    Variables: 
    '''
    def __init__(self):
        self._gridLineColor = Color('black')
        self._screenBackground = pygame.Color('gray')
        self._gridHeight = 25
        self._gridWidth = 25
        self._gridCellSize = 16

        pygame.init()

        self.flags = pygame.RESIZABLE
        self.rect = pygame.Rect(0, 0, 600, 600)
        self.screen = pygame.display.set_mode(self.rect.size, self.flags)

        self.fps = 60

        '''
        Parameters for perlin noise generator
        '''
        self.octaves = 10
        self.seedPerlin = 35
        self.noise = PerlinNoise(octaves=self.octaves, seed=self.seedPerlin)

        self.running = True 

    def noiseGridGenerator(self):
        self.noiseGrid = [[int(self.noise([i/self._gridWidth, j/self._gridHeight]) * 10) for i in range(self._gridWidth)] for j in range(self._gridHeight)]


    '''
    Pygame draws object in order,
    the function below decides the order of the draw
    '''
    def draw(self):
        self.screen.fill(self._screenBackground)
        self.drawGrid()

        pygame.display.update()



    def run(self):

        self.clock = pygame.time.Clock()

        self.noiseGridGenerator()

        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()
        pygame.quit()

    def drawGrid(self):

        for x in range(self._gridWidth):
            for y in range(self._gridHeight):
                rect = pygame.Rect(x * self._gridCellSize, y * self._gridCellSize, self._gridCellSize, self._gridCellSize)
                rectText = str(self.noiseGrid[x][y])
                img, rectText = Text(rectText, pos=( (x * self._gridCellSize) + 2, (y * self._gridCellSize) +2)).render()
                pygame.draw.rect(self.screen, self._gridLineColor, rect, 1)
                self.screen.blit(img, rectText)
