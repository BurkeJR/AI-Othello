
class piece:
    def __init__(self, index):
        self.color = '*'
        self.location: tuple(int, int) = index

    def __str__(self):
        return self.color
    
    def __eq__(self, other):
        return self.color == other