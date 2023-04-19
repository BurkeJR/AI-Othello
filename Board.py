from Piece import piece

class board:
    def __init__(self):
        """8x8 board with starting pieces of
        W B
        B W"""
        self.board = self.makeBoard()


    def makeBoard(self) -> list[list[piece]]:
        emptyBoard = [[piece for _ in range(8)] for _ in  range(8)]
        emptyBoard[3][3].color = 'W'
        emptyBoard[3][4].color = 'B'
        emptyBoard[4][3].color = 'B'
        emptyBoard[4][4].color = 'W'
        return emptyBoard
    
    def __str__(self):
        stringBuilder: str = ""
        for row in self.board:
            for val in row:
                stringBuilder += str(val)
            stringBuilder += '\n'
        return stringBuilder

    def __repr__(self) -> str:
        return str(self)

Board = board
print(Board)