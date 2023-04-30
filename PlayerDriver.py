from Board import board
from Heuristic import count

class player():
    

    def __init__(self) -> None:
        self.colMap = {1: 'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
        pass

    def run(self):
        game = board()

        while not game.isWon() and not game.isFull():
            print(game)
            moves = self.getMoves(game)

            if len(moves) == 0:
                print(f"No moves for {game.currentPlayer}, move forfeited")
                if game.currentPlayer == 'W':
                    game.currentPlayer = 'B'
                else:
                    game.currentPlayer == 'W'
                continue

            print(f"{game.currentPlayer}'s move.")
            print(moves)



            row = col = 0
            getResponse = True
            while getResponse:
                try:
                    response = input("Select move to make 'row,col': ").strip()
                    vals = response.split(',')
                    row = int(vals[0].strip()) - 1
                    col = list(self.colMap.keys())[list(self.colMap.values()).index(vals[1].strip())] - 1
                    getResponse = False
                except Exception as e:
                    print(str(e))
                    print("Try again")

            game = self.makeMove(game, (row, col))
            if game.currentPlayer == 'W':
                game.currentPlayer = 'B'
            else:
                game.currentPlayer = 'W'

        stringBuilder = str(game)
        bScore = count(game, 'B')
        wScore = count(game, 'W')
        stringBuilder +=  f"{bScore} - {wScore}"
        if bScore > wScore:
            stringBuilder += "B won!"
        elif wScore > bScore:
            stringBuilder += "W won!"
        else:
            stringBuilder += "It's a tie!"
        return stringBuilder
        

    def getMoves(self, game: board):
        moves = set()
        for spot in game.getAllPlayableSpots():
            for row,col in spot:
                if len(spot) == 1: continue
                if game.gameBoard[row][col] == '*':
                    moves.add((row + 1, self.colMap[col + 1]))

        return moves
    
    def makeMove(self, game: board, location):
        for spot in game.getAllPlayableSpots():
            if len(spot) == 1: continue
            if location in spot:
                for row,col in spot:
                    game.gameBoard[row][col].color = game.currentPlayer
                break
        return game

