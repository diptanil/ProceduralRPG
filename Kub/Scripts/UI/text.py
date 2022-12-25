import pygame
from pygame.locals import *

from ..Lookups.lookups import *

class Text():
    """Create a text object."""

    def __init__(self, text, pos, fontcolor = COLOR_BLACK):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 16
        self.fontcolor = fontcolor
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font object from //fontname and //fontsize"""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image using //fontcolor"""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        return self.img, self.rect
        