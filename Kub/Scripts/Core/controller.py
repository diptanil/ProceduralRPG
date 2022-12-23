import pygame
from pygame.locals import *

class Controller:
    def __init__(self, debug = False):
        self.debug = debug


        if self.debug:
            print("Debug Controller")

    def toggle_fullscreen(self, app):
        app.flags ^= FULLSCREEN
        pygame.display.set_mode((0,0), app.flags)

