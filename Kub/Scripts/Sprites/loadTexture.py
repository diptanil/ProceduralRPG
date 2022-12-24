from ..Lookups.lookups import *
from .spritesheetLoader import SpritesheetLoader

class LoadTextures:

    def __init__(self, category, colorkey = None):
        self.Textures = {}

        files = list(SPRITES[category].keys())
        for filename in files:
            sprites = SpritesheetLoader(filename, category).load(colorkey)
            for key in list(sprites.keys()):
                self.Textures[key] = sprites[key]
