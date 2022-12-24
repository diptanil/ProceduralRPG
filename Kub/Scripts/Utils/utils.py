from dataclasses import dataclass


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