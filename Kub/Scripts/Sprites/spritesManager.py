from .loadTexture import LoadTextures

class SpritesManager:
    def __init__(self):
        self.terrainTextures = LoadTextures(category="terrain").Textures
        self.vegetationTextures = LoadTextures(category="vegetation").Textures