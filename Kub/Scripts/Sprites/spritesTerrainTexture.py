from ..Lookups.lookups import *
from .spritesheetLoader import SpritesheetLoader

class LoadTerrainTextures:

    def __init__(self):
        self.terrainTextures = {}

        category = "terrain"

        files = list(SPRITES[category].keys())
        for filename in files:
            sprites = SpritesheetLoader(filename, category).load()
            for key in list(sprites.keys()):
                self.terrainTextures[key] = sprites[key]
