import pygame
from .text import Text

from ..Lookups.lookups import *
from ..Utils import *

class InfoBox:
    def __init__(self, pos, width, height):
        self.position = pos
        self.rect = pygame.Rect(pos.x, pos.y, width, height)

        self.rightMargin = 20
        self.topMargin = 10

    
    def Render(self, screen):
        '''
        Rendering background
        '''
        pygame.draw.rect(screen, COLOR_INFOBOX_BACKGROUND, self.rect)

        '''
        Rendering all the texts
        '''
        for infoText in INFORMATION:
            img, rectText  = Text(infoText.text, pos=(self.position.x + self.rightMargin,
                                    self.position.y + self.topMargin), 
                                    fontcolor=infoText.fontcolor).render()
            
            screen.blit(img, rectText)
