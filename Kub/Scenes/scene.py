import pygame

class Scene:
    '''
    Create new scenes
    '''
    id = 0
    background = pygame.Color('gray')

    def __init__(self, app):
        self.app = app
        self.app.scenes.append(self)
        self.app.scene = self

        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.background = Scene.background

    def draw(self):
        self.app.screen.fill(self.background)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

    def __str__(self) -> str:
        return 'Scene {}'.format(self.id)