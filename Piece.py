
class piece:
    def __init__(self, index):
        self.occupied = False
        self.white = False
        self.black = False
        self.location: tuple(int, int) = index

    def __str__(self):
        return self.color
    
    def __eq__(self, other):
        return self.color == other


    @property
    def color(self) -> str:
        if self.white:
            return 'W'
        if self.black:
            return 'B'
        return '*'
    @color.setter
    def color(self, color: str):
        if color == 'W':
            self.white = True
            self.black = False
        elif color == 'B':
            self.black = True
            self.white = False
        else:
            raise ValueError("Cannot set piece to color other than White ('W') or Black ('B')")
        self.occupied = True