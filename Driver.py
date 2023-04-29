from Board import board
from Heuristic import coinParity, cornersCaptured
import copy

def main():
    blackAI = cornersCaptured()
    whiteAI = coinParity()
    bestBoard: board = board(blackAI=blackAI, whiteAI=whiteAI)
    

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
        max = -100
        bestBoard = game
        for b in derivedBoards(game):
            b.currentPlayer = 'W'
            bestBoard = minimax(b,depth + 1)
            val = game.blackAI.evaluate(bestBoard)
            if val > max:
                max = val
                bestBoard = b
        return bestBoard
    else:
        min = 100
        bestBoard = game
        for b in derivedBoards(game):
            b.currentPlayer = 'B'
            bestBoard = minimax(b,depth + 1)
            val = game.whiteAI.evaluate(bestBoard)
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

main()