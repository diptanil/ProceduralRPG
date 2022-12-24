from ..Lookups.lookups import *
from .spritesheetAnimator import SpritesheetAnimator

class LoadAnimations:
    '''

    '''
    def __init__(self, category, AnimationFPS = 4, bloop = True, colorkey = None):
        frames = FPS/AnimationFPS
        filename = list(SPRITES[category].keys())[0]
        self.Animation = SpritesheetAnimator(filename, category, colorkey = colorkey, bloop=bloop, frames=frames)
        # files = list(SPRITES[category].keys())
        # for filename in files:
        #     self.Animations[category] = SpritesheetAnimator(filename, category, colorkey = colorkey, bloop=bloop, frames=frames)
            # for key in list(sprites.keys()):
            #     self.Textures[key] = sprites[key]
