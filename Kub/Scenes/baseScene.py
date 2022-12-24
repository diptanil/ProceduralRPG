class BaseScene:
    def __init__(self):
        self.next = self
        
    def ProcessInput(self, events, pressed_keys):
        print("WARNING!!! you didn't override the " + 
        "Process Input function of the child class")
        
    def Update(self):
        print("WARNING!!! you didn't override the " + 
        "Update function of the child class")
    
    def Render(self, screen):
        print("WARNING!!! you didn't override the " + 
        "Update function of the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)