from Board import board
from Heuristic import count

class player():
    def __init__(self) -> None:
        pass

    def run(self):
        game = board()

        while not game.isWon() and not game.isFull():
            print(game)
            moves = self.getMoves(game)
            print(moves)

            response = input("Select move to make: ")

        stringBuilder = str(game)
        stringBuilder +=  f"{count(game, 'B')} - {count(game, 'W')}\n"
        return stringBuilder
        

    def getMoves(self, game: board):
        colMap = {1: 'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}

        moves = set()
        for spot in game.getAllPlayableSpots():
            if len(spot) == 1: continue
            row, col = list(spot)[1]
            moves.add((row + 1, colMap[col+1]))
        return moves

