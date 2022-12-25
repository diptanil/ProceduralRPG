from dataclasses import dataclass
from ..Lookups.lookups import *


@dataclass
class XYPos:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, XYPos):
            if self.x == __o.x and self.y == __o.y:
                return True
        return False

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __str__(self) -> str:
        return "(" + str(self.x) + " ," + str(self.y) + " )"

'''
Info box data structure for storing the text along 
with their fontcolor (dependent upon their type)
'''
@dataclass
class InfoBoxText:
    def __init__(self, text, msgType = None):

        self.text = text

        if msgType == "vegetation":
            self.fontcolor = COLOR_VEGETATION
        elif msgType == "waterbody":
            self.fontcolor = COLOR_WATERBODY
        else:
            self.fontcolor = COLOR_INFOBOX_MESSAGE

'''
All the information that is available in the
Info Box.
'''
class Information:
    def __init__(self):
        self.information = []
    
    def addInformation(self, text, msgType = None):
        self.information.append(InfoBoxText(text, msgType=msgType))
    
    def clearInformation(self):
        self.information = []


