from ..Utils.utils import *

TERRAIN_TEXTURE_SPRITES = {
    "Ground/Grass.png": {
        "water": XYPos(0, 0),
        "grass-light": XYPos(1, 0),
        "grass-dark": XYPos(2, 0),
        "ground-dirt1": XYPos(3, 0),
        "ground-dirt2": XYPos(4, 0),
    },
    "Ground/Shore.png": {
        "sand": XYPos(0, 0),
        "wet-sand": XYPos(1, 0),
        "shallow-water": XYPos(2, 0),
        # Position 3 is same as water for Ground/Grass.png
        "deep-water": XYPos(4, 0),
    },
    "Ground/Winter.png": {
        "deep-water-winter": XYPos(0, 0),
        # Position 1 is same as water for Ground/Grass.png
        "shallow-water-winter": XYPos(2, 0),
        "wet-sand-winter": XYPos(3, 0),
        "snow": XYPos(4, 0),
        "rock": XYPos(5, 0),
        "grass-dark-winter": XYPos(6, 0),
        "grass-light-winter": XYPos(7, 0),
    },
}

VEGETATION_SPRITES = {
    "Nature/Trees.png": {
        "tree-trunk": XYPos(0, 0),
        "tree-bel": XYPos(1, 0),
        "tree-ashoka": XYPos(2, 0),
        "tree-mango": XYPos(3, 0),
    },
    "Nature/CoconutTrees.png": {
        "cocotree-right-trunk": XYPos(0, 0),
        "cocotree-left-trunk": XYPos(1, 0),
        "cocotree-right": XYPos(2, 0),
        "cocotree-right-fruit": XYPos(3, 0),
        "cocotree-left": XYPos(4, 0),
        "cocotree-left-fruit": XYPos(5, 0),
    },
}

SPRITES = {
    "terrain":  TERRAIN_TEXTURE_SPRITES,
    "vegetation": VEGETATION_SPRITES,
}

