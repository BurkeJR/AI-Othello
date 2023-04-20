from Board import board
from Piece import piece
import copy

def main():
    gameBoard: board = board()

    bestBoard = minimax(gameBoard, 0)

    print(bestBoard)

MAX_DEPTH = 4

def minimax(game: board, depth) -> board:
    if game.isFull() or depth == MAX_DEPTH:
        if game.currentPlayer == 'W':
            #Max
            max = 0
            bestBoard = board(blank = True)
            for b in derivedBoards(game):
                b.currentPlayer = 'B'
                val = evaluate(b)
                if val > max:
                    max = val
                    bestBoard = b
            return bestBoard
        else:
            #Min
            min = 8 * 8
            bestBoard = board(blank = True)
            for b in derivedBoards(game):
                b.currentPlayer = 'W'
                val = evaluate(b)
                if val < min:
                    min = val
                    bestBoard = b
            return bestBoard
    
    if game.currentPlayer == 'W':
        max = 0
        bestBoard = board(blank = True)
        for b in derivedBoards(game):
            b.currentPlayer = 'B'
            bestBoard = minimax(b,depth + 1)
            val = evaluate(bestBoard)
            if val > max:
                max = val
                bestBoard = b
        return bestBoard
    else:
        min = 8*8
        bestBoard = board(blank = True)
        for b in derivedBoards(game):
            b.currentPlayer = 'W'
            bestBoard = minimax(b,depth + 1)
            val = evaluate(bestBoard)
            if val < min:
                min = val
                bestBoard = b
        return bestBoard

def derivedBoards(game: board) -> list[board]:
    boardList: list[board] = list()
    for spots in game.getAllPlayableSpots():
        newBoard = copy.deepcopy(game)
        if len(spots) == 1: continue
        for row,col in spots:
            newBoard.gameBoard[row][col].color = game.currentPlayer
        boardList.append(newBoard)

    return boardList


    


def evaluate(game: board) -> int:
    """If white, returns number of white tiles
    If black, returns fraction of tiles that are """
    if game.currentPlayer == 'W':
        return count(game, 'W')
    else:
        return count(game, 'B')

def count(game: board, color):
    count = 0
    for row in game.gameBoard:
        for val in row:
            if val == color:
                count += 1
    return count




main()