from ..Lookups.lookups import *
from .spritesheetLoader import SpritesheetLoader

class LoadTextures:

    def __init__(self, category):
        self.Textures = {}

        # category = "terrain"

        files = list(SPRITES[category].keys())
        for filename in files:
            if category == "terrain":
                sprites = SpritesheetLoader(filename, category).load()
            else:
                sprites = SpritesheetLoader(filename, category).load(colorkey=-1)
            for key in list(sprites.keys()):
                self.Textures[key] = sprites[key]
