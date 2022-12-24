from .spritesheetLoader import SpritesheetLoader

class SpritesheetAnimator:
    '''
    bloop is a boolean that, when True, causes the next() method to
    loop. If False, the terminal case raises StopIteration. 
    Set it to true for animation to repeat

    frames is the number of ticks to return the same image before
    the iterator advances to the next image.
    '''
    def __init__(self, filename, category, colorkey=None, bloop=False, frames =1):
        self.filename = filename
        spritesheet = SpritesheetLoader(filename, category)
        self.sprites = spritesheet.loadAsList(colorkey)

        self.i = 0
        self.bloop = bloop

        self.frames = frames
        self.f = self.frames
    
    def iter(self):
        self.i = 0
        self.f = self.frames
        return self
    
    def next(self):
        if self.i >= len(self.sprites):
            if not self.bloop:
                raise StopIteration
            else:
                self.i = 0
        
        sprite = self.sprites[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return sprite

    def __add__(self, sprites):
        self.sprites.extend(sprites)
        return self
