from .loadTexture import LoadTextures
from .loadAnimations import LoadAnimations

class SpritesManager:
    def __init__(self):
        self.terrainTextures = LoadTextures(category="terrain").Textures
        # self.terrainTextures = None
        self.vegetationTextures = LoadTextures(category="vegetation", colorkey=-1).Textures
        # self.vegetationTextures = None
        self.boxSelectAnim = LoadAnimations(category="UI-boxselector", AnimationFPS=6, bloop=True, colorkey=-1).Animation
        # self.boxSelectAnim = None