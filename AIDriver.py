from Board import board
from Heuristic import count
import copy



class aiDriver():
    def __init__(self, blackAI, whiteAI, MAX_DEPTH = 4) -> None:
        self.blackAI = blackAI
        self.whiteAI = whiteAI
        self.MAX_DEPTH = MAX_DEPTH
    
    def run(self) -> str:
        stringBuilder: str = ""
        bestBoard = board(blackAI=self.blackAI, whiteAI=self.whiteAI)

        while bestBoard.continueGame:
            bestBoard = self.minimax(bestBoard, 0)
            stringBuilder += str(bestBoard)
            stringBuilder += '\n\n'
    
        stringBuilder += f"{count(bestBoard, 'B')} - {count(bestBoard, 'W')}"

        return stringBuilder

    def minimax(self, game: board, depth) -> board:
        if depth == self.MAX_DEPTH:
            return game

        if game.isWon() or game.isFull():
            game.continueGame = False
            return game
    
        if game.noMoves():
            if game.currentPlayer == 'W':
                game.currentPlayer = 'B'
            else:
                game.currentPlayer = 'W'
            return self.minimax(game, depth + 1)
    
        if game.currentPlayer == 'B':
            max = -10000
            bestBoard = game
            for b in self.derivedBoards(game):
                b.currentPlayer = 'W'
                best = self.minimax(b,depth + 1)
                val = game.blackAI.evaluate(best)
                if val > max:
                    max = val
                    bestBoard = best
            return bestBoard
        else:
            min = 10000
            bestBoard = game
            for b in self.derivedBoards(game):
                b.currentPlayer = 'B'
                best = self.minimax(b,depth + 1)
                val = game.whiteAI.evaluate(best)
                if val < min:
                    min = val
                    bestBoard = best
            return bestBoard

    def derivedBoards(self, game: board) -> list[board]:
        boardList: list[board] = list()
        for spots in game.getAllPlayableSpots():
            newBoard = copy.deepcopy(game)
            if len(spots) == 1: continue
            for row,col in spots:
                newBoard.gameBoard[row][col].color = game.currentPlayer
            boardList.append(newBoard)

        return boardList


