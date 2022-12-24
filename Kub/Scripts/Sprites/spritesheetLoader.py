import os
import pygame

from ..Lookups.lookups import *
from ..Utils.utils import *

class SpritesheetLoader:
    def __init__(self, filename, category):
        self.filename = filename
        self.category = category
        self.exists = False
        try:
            self.sprite_image = pygame.image.load(
                os.path.join(SPRITES_FOLDER, self.filename)
                )
            self.exists = True
        except:
            raise FileExistsError("Unable to load spritesheet")

    def load_sprite(self, pos: XYPos, colorkey = None):
        x = pos.x * SPRITE_SIZE
        y = pos.y * SPRITE_SIZE
        rect = pygame.Rect(x, y, SPRITE_SIZE, SPRITE_SIZE)
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
            for sp in list(SPRITES[self.category][self.filename].keys()):
                self.sprites[sp] = self.load_sprite(
                    SPRITES[self.category][self.filename][sp]
                )
        return self.sprites 