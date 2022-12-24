from .app import App
# from .Core.proceduralWorldGenerator import ProceduralWorldGenerator
from .Temp.proceduralGridGeneration import ProceduralGridGeneration
def main():
    # print("Initial Setup Complete")
    # ProceduralGridGeneration().run()
    app = App()
    app.run()
