from abc import ABC, abstractmethod

class heuristic(ABC):

    @abstractmethod
    def evaluate(self, board) -> int:
        pass

class coinParity(heuristic):
    def count(self, game, color):
        count = 0
        for row in game.gameBoard:
            for val in row:
                if val == color:
                    count += 1
        return count


    def evaluate(self, board) -> int:

        maxCount = self.count(board, 'B')
        minCount = self.count(board, 'W')
        total = maxCount + minCount

        return ((maxCount - minCount) / total) * 100
