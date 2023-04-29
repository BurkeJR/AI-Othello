from Heuristic import heuristic

class ai():
    def __init__(self, heuristic: heuristic, color):
        self.heuristic = heuristic
        self.color = color

    def evaluate(self, board):
        return self.heuristic.evaluate(board)
    
    

