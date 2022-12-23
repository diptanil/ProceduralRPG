import pygame
from pygame.locals import *
import numpy as np
import noise

class Text():
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

        self.running = True 

    def noiseGridGenerator(self, density):
        self.noiseGrid = [[0 for i in range(self._gridWidth)] for j in range(self._gridHeight)]
        for x in range(self._gridWidth):
            for y in range(self._gridHeight):
                pass

    def run(self):

        self.clock = pygame.time.Clock()

        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(self._screenBackground)
            self.drawGrid()
            pygame.display.update()

        pygame.quit()

    def drawGrid(self):
        for x in range(0, self._gridWidth * self._gridCellSize, self._gridCellSize):
            for y in range(0, self._gridHeight * self._gridCellSize, self._gridCellSize):
                rect = pygame.Rect(x, y, self._gridCellSize, self._gridCellSize)
                rectText = "1"
                img, rectText = Text(rectText, pos=(x +2, y +2)).render()
                pygame.draw.rect(self.screen, self._gridLineColor, rect, 1)
                self.screen.blit(img, rectText)
