from ..Lookups.lookups import *
from perlin_noise import PerlinNoise

class ProceduralWorldGenerator:
    def __init__(self, octaves = 4, seed = 2):
        print("Running procedural world generator")

        '''
        Setting up Perlin noise using the parameters
        octaves - 
        seed - 
        '''
        self.noise = PerlinNoise(octaves=octaves, seed=seed)
        self.noiseGridGenerator()


    '''
    Generating a noise grid of GRID_WIDTH x GRID_HEIGHT
    using Perlin noise
    '''
    def noiseGridGenerator(self):
        self.noiseGrid = [[self.noise([i/GRID_WIDTH, 
        j/GRID_HEIGHT]) for i in range(GRID_WIDTH)] 
        for j in range(GRID_HEIGHT)]
