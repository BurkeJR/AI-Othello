from Piece import piece


class board:
    def __init__(self):
        """8x8 board with starting pieces of
        W B
        B W"""

        self.gameBoard: list[list[piece]] = self.makeBoard()
        self.currentPlayer = 'W'


    def makeBoard(self) -> list[list[piece]]:
        emptyBoard = [[piece((row, col)) for col in range(8)] for row in  range(8)]
        emptyBoard[3][3].color = 'W'
        emptyBoard[3][4].color = 'B'
        emptyBoard[4][3].color = 'B'
        emptyBoard[4][4].color = 'W'
        return emptyBoard
    
    def isValidIndex(self, row: int, col: int) -> bool:
        if row < 0 or col < 0:
            return False
        if row > 7 or col > 7:
            return False
        return True
    
    def getFlippableTiles(self, tile: piece, rowStart: int, colStart: int):
        """Takes a tile on the board, and checks to see if there are any spots around it that can be flipped.
        Returns False if tile cannot be flipped, else returns list of tiles that would be flipped"""
        if self.gameBoard[rowStart][colStart] != "*":
            return False
        
        self.gameBoard[rowStart][colStart] = tile

        otherPlayerColor = ''
        
        if self.currentPlayer == 'W':
            otherPlayerColor = 'B'
        else:
            otherPlayerColor = 'W'

        flippableTiles: list[tuple] = list()
        
        for rowIncrement, colIncrement in [(0,1), (1,1), (1,0), (0, -1), (-1,-1), (-1,0), (-1,1), (1,-1)]:
            row, col = rowStart, colStart
            row += rowIncrement
            col += colIncrement
            while self.isValidIndex(row, col) and self.gameBoard[row][col] == otherPlayerColor:
                row += rowIncrement
                col += colIncrement

            if not self.isValidIndex(row, col):
                continue

            if self.gameBoard[row][col] == self.currentPlayer:
                while True:
                    row -= rowIncrement
                    col -= colIncrement
                    if row == rowStart and col == colStart:
                        flippableTiles.append((row,col))
                        break
                    flippableTiles.append((row,col))

        self.gameBoard[rowStart][colStart] = piece((rowStart,colStart))

        if len(flippableTiles) > 0:
            return flippableTiles
        return False


    def getAllPlayableSpots(self) -> list[list[tuple]]:
        allPlayableSpots: list[list[tuple]] = list()

        for row in self.gameBoard:
            for val in row:
                tileRow, tileCol = val.location
                playableTile = self.getFlippableTiles(val, tileRow, tileCol)

                if not playableTile:
                    continue

                allPlayableSpots.append(playableTile)

        return allPlayableSpots


    
    
    def __str__(self):
        stringBuilder: str = ""
        for row in self.gameBoard:
            for val in row:
                stringBuilder += str(val) + ' '
            stringBuilder += '\n'
        return stringBuilder

    def __repr__(self) -> str:
        return str(self)
    
    def isFull(self):
        return self.gameBoard.count('*') == 0
    
