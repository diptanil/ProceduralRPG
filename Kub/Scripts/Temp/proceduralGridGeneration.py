import os

import pygame
from pygame.locals import *
import numpy as np
from perlin_noise import PerlinNoise

from ..Lookups.lookups import *
from ..Utils.utils import *

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


class SpritesheetLoader:
    def __init__(self, filename):
        self.filename = filename
        self.exists = False
        try:
            self.sprite_image = pygame.image.load(
                os.path.join(SPRITES_FOLDER, self.filename)
                )
            self.exists = True
        except:
            raise FileExistsError("Unable to load spritesheet")

    def load_sprite(self, pos: XYPos, colorkey = None):
        rect = pygame.Rect(pos.x, pos.y, SPRITE_SIZE, SPRITE_SIZE)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sprite_image, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def load(self, colorkey = None):
        self.sprites = {}
        if self.exists:
            for sp in list(SPRITES[self.filename].keys()):
                self.sprites[sp] = self.load_sprite(
                    SPRITES[self.filename][sp]
                )
        return self.sprites


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
        self.groundTexture = SpritesheetLoader("Ground/Grass.png").load()

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
                rectValue = self.noiseGrid[x][y]
                img, rectText = Text(str(rectValue), pos=( (x * self._gridCellSize) + 2, (y * self._gridCellSize) +2)).render()
                pygame.draw.rect(self.screen, self._gridLineColor, rect, 1)
                if rectValue == 0:
                    self.screen.blit(self.groundTexture['Water'], (x * self._gridCellSize, y * self._gridCellSize))
                else:
                    self.screen.blit(img, rectText)
