from Piece import piece
from AI import ai


class board:
    def __init__(self, blank = False, blackAI: ai = None, whiteAI: ai = None):
        """8x8 board with starting pieces of
        W B
        B W"""
        if blank:
            self.gameBoard = [[piece((row, col)) for col in range(8)] for row in range(8)]
        else:
            self.gameBoard: list[list[piece]] = self.makeBoard()

        if blackAI == None:
            self.isAI = False
        else:
            self.isAI = True
        
        self.blackAI = blackAI
        self.whiteAI = whiteAI            
        self.currentPlayer = 'B'
        self.continueGame = True


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
    
    def getFlipTiles(self, tile: piece, rowStart: int, colStart: int):
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

        changeableTiles: set[tuple] = set()
        
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
                        changeableTiles.add((row,col))
                        break
                    changeableTiles.add((row,col))

        self.gameBoard[rowStart][colStart] = piece((rowStart,colStart))

        if len(changeableTiles) > 0:
            return changeableTiles
        return False


    def getAllPlayableSpots(self) -> list[set[tuple]]:
        allPlayableSpots: list[set[tuple]] = list()

        for row in self.gameBoard:
            for val in row:
                tileRow, tileCol = val.location
                playableTile = self.getFlipTiles(val, tileRow, tileCol)

                if not playableTile:
                    continue

                allPlayableSpots.append(playableTile)

        return allPlayableSpots


    
    
    def __str__(self):
        stringBuilder: str = "A B C D E F G H\n"
        count = 1
        for row in self.gameBoard:
            stringBuilder += str(count) + ' '
            count += 1
            for val in row:
                stringBuilder += str(val) + ' '
            stringBuilder += '\n'
        return stringBuilder

    def __repr__(self) -> str:
        return str(self)
    
    def isFull(self):
        for row in self.gameBoard:
            for val in row:
                if val == '*':
                    return False
        return True
                
    def isWon(self):
        countAll = 0
        countW = 0
        countB = 0
        for row in self.gameBoard:
            for val in row:
                if val == 'W':
                    countAll += 1
                    countW += 1
                elif val == 'B':
                    countAll += 1
                    countB += 1

        if countW == countAll:
            return True
        if countB == countAll:
            return True
        return False
        
    def noMoves(self):
        for spots in self.getAllPlayableSpots():
            if len(spots) == 1:
                continue
            else:
                return False
        return True
    
