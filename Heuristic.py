from abc import ABC, abstractmethod
from Piece import piece
from Board import board
import copy


def count(game, color):
        count = 0
        for row in game.gameBoard:
            for val in row:
                if val == color:
                    count += 1
        return count

class heuristic(ABC):

    @abstractmethod
    def evaluate(self, board) -> int:
        pass

class coinParity(heuristic):
    def evaluate(self, board) -> int:

        maxCount = count(board, 'B')
        minCount = count(board, 'W')
        total = maxCount + minCount

        return ((maxCount - minCount) / total) * 100
    
    def __str__(self) -> str:
        return "Coin Parity"
    
class cornersCaptured(heuristic):
    def heldCorners(self, board, color) -> int:
        count = 0
        if board.gameBoard[0][0] == color:
            count += 1
        if board.gameBoard[0][7] == color:
            count+= 1
        if board.gameBoard[7][0] == color:
            count+=1
        if board.gameBoard[7][7] == color:
            count+=1
        return count

    def closeCorners(self, board, color) -> int:
        """Evaluates whether player of color color holds any tiles nearby to corners"""
        count = 0
        grid = board.gameBoard
        
        if grid[0][0] == '*':
            if grid[0][1] == color: count += 1
            if grid[1][1] == color: count += 1
            if grid[1][0] == color: count += 1
        if grid[0][7] == '*':
            if grid[0][6] == color: count += 1
            if grid[1][6] == color: count += 1
            if grid[1][7] == color: count += 1
        if grid[7][0] == '*':
            if grid[7][1] == color: count += 1
            if grid[6][1] == color: count += 1
            if grid[6][0] == color: count += 1
        if grid[7][7] == '*':
            if grid[6][7] == color: count += 1
            if grid[6][6] == color: count += 1
            if grid[7][6] == color: count += 1
        return count
		    
    def evaluate(self, board) -> int:
        closeW = self.closeCorners(board, 'W')
        closeB = self.closeCorners(board, 'B')
        maxCornerVal = self.heldCorners(board, 'B') + (.25 * closeW) - (.25 * closeB)
        minCornerVal = self.heldCorners(board, 'W') + (.25 * closeB) - (.25 * closeW)
        total = maxCornerVal + minCornerVal

        if total != 0:
            return ((maxCornerVal - minCornerVal) / total) * 100
        return 0
    
    def __str__(self) -> str:
        return "Corners Captured"
    
class mobility(heuristic):
    def evaluate(self, board) -> int:
        maxCount = self.numMoves(board, 'B')
        maxCount += .1 * self.emptySpaces(board, 'B')

        minCount = self.numMoves(board, 'W')
        minCount += .1 * self.emptySpaces(board, 'W')

        total = maxCount + minCount

        if total == 0:
            return 0

        return ((maxCount - minCount) / total) * 100

    def numMoves(self, board, color) -> int:
        board = copy.deepcopy(board)
        board.currentPlayer = color
        count = 0
        for spot in board.getAllPlayableSpots():
            if len(spot) == 1: continue
            count += 1
        return count
    
    def emptySpaces(self, board, color) -> int:
        count = 0
        grid = copy.deepcopy(board).gameBoard
        for gridRow in grid:
            for val in gridRow:
                (row, col) = val.location
                if grid[row][col] == color:
                    count += self.empty(row, col, grid)

        return count
    
    def empty(self, row, col, grid):
        count = 0

        if row != 0:
            if grid[row-1][col] == '*': count+=1
            if col != 0:
                if grid[row - 1][col - 1] == '*': count+=1
            if col != 7:
                if grid[row - 1][col + 1] == '*': count+=1
        if row !=7:
            if grid[row+1][col] == '*': count+=1
            if col != 0:
                if grid[row+1][col-1] == '*': count+=1
            if col != 7:
                if grid[row+1][col+1] == '*': count+=1
        if col != 0:
            if grid[row][col-1] == '*': count+=1
        if col != 7:
            if grid[row][col+1] == '*': count+=1

        return count
    
    def __str__(self) -> str:
        return "Mobility"

class stability(heuristic):
    def evaluate(self, board) -> int:
        board = copy.deepcopy(board)
        maxCount =  4 * self.stableCount(board, 'B')
        maxCount -= 2 * self.unstableCount(board, 'W') #2 modifier to account for 1 in stableCount

        
        minCount = 4 * self.stableCount(board, 'W')
        minCount -= 2 * self.unstableCount(board, 'B') #2 modifier to account for 1 in stableCount

        total = maxCount + minCount

        if total == 0:
            return 0

        return ((maxCount - minCount) / total) * 100 
    
    def stableCount(self, board: board, color):
        count = 0
        board.currentPlayer = color

        for row in board.gameBoard:
            for val in row:
                if val == color:
                    if self.checkStability(board, val.location, color):
                        #Stable tiles are worth 4
                        count += 1
                    else:
                        #Semi or Unstable worth 1
                        #Makes Unstable worth -1 once final calculation done
                        count += .25

        return count
    
    def checkStability(self, board: board, location: tuple, color):
        startRow, startCol = location
        grid = board.gameBoard

        rowStable = False
        colStable = False

        row = startRow
        col = startCol
        
        if row == 0 or row == 7:
            colStable = True
        if col == 0 or col == 7:
            rowStable = True
        
        while not rowStable:
            #Move left
            col -= 1
            if col < 0:
                rowStable = True
                break
            if grid[row][col] != color:
                break
            
        row = startRow
        col = startCol
        while not rowStable:
            #Move Right
            col += 1
            if col > 7:
                rowStable = True
                break
            if grid[row][col] != color:
                break
        

        row = startRow
        col = startCol
        while not colStable:
            #Move Up
            row -= 1
            if row < 0:
                colStable = True
                break
            if grid[row][col] != color:
                break
        
        row = startRow
        col = startCol
        while not colStable:
            #Move Down
            row += 1
            if row > 7:
                colStable = True
                break
            if grid[row][col] != color:
                break

        return rowStable and colStable
    
    def unstableCount(self, board: board, color: str):
        count = 0
        board.currentPlayer = color
        unstable = set()
        for spot in board.getAllPlayableSpots():
            if len(spot) == 1: continue

            for location in spot:
                unstable.add(location)
            count += 1

        return len(unstable) - count
    
    def __str__(self) -> str:
        return "Stability"