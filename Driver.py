from Board import board
from Piece import piece
import copy

def main():
    bestBoard: board = board()
    

    while bestBoard.continueGame:
        bestBoard = minimax(bestBoard, 0)
        print(bestBoard)
    
    score = f"{count(bestBoard, 'B')} - {count(bestBoard, 'W')}"

    print(bestBoard)

    print(score)

MAX_DEPTH = 5

def minimax(game: board, depth) -> board:
    if depth == MAX_DEPTH:
        return game

    if game.isWon() or game.isFull():
        game.continueGame = False
        return game
    
    if game.noMoves():
        if game.currentPlayer == 'W':
            game.currentPlayer = 'B'
        else:
            game.currentPlayer = 'W'
        return minimax(game, depth + 1)
    
    if game.currentPlayer == 'B':
        max = 0
        bestBoard = game
        for b in derivedBoards(game):
            b.currentPlayer = 'W'
            bestBoard = minimax(b,depth + 1)
            val = evaluate(bestBoard)
            if val > max:
                max = val
                bestBoard = b
        return bestBoard
    else:
        min = 8*8
        bestBoard = game
        for b in derivedBoards(game):
            b.currentPlayer = 'B'
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