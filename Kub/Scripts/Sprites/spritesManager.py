from .spritesTerrainTexture import LoadTerrainTextures

class SpritesManager:
    def __init__(self):
        self.terrainTextures = LoadTerrainTextures().terrainTextures