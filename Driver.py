from Board import board
from Piece import piece
import copy

def main():
    gameBoard: board = board()

    print(gameBoard)


    boardList: list[board] = list()

    for spots in gameBoard.getAllPlayableSpots():
        newBoard = copy.deepcopy(gameBoard)
        if len(spots) == 1: continue
        for row,col in spots:
            newBoard.gameBoard[row][col].color = 'W'
        boardList.append(newBoard)


    for b in boardList:
        print(b)



def minimax(game: board) -> board:

    

    return game







main()