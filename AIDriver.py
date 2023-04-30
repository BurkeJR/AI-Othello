from Board import board
from Heuristic import count
import copy


class aiDriver():
    def __init__(self, blackAI, whiteAI, MAX_DEPTH = 5, wordy = True) -> None:
        self.blackAI = blackAI
        self.whiteAI  = whiteAI
        self.MAX_DEPTH = MAX_DEPTH
        self.wordy = wordy
    
    def run(self) -> str:
        stringBuilder: str = ""
        bestBoard = board(blackAI=self.blackAI, whiteAI=self.whiteAI)

        while bestBoard.continueGame:
            bestBoard = self.minimax(bestBoard, 0, -10000, 10000)
            if (self.wordy):
                stringBuilder += str(bestBoard)
                stringBuilder += str(bestBoard.blackAI.evaluate(bestBoard))
                stringBuilder += '\n\n'
    
        stringBuilder += f"{count(bestBoard, 'B')} - {count(bestBoard, 'W')}"

        return stringBuilder

    def minimax(self, game: board, depth, alpha, beta) -> board:
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
            return self.minimax(game, depth + 1, alpha, beta)
    
        if game.currentPlayer == 'B':
            maxVal= -10000
            bestBoard = game
            for b in self.derivedBoards(game):
                b.currentPlayer = 'W'
                best = self.minimax(b,depth + 1, alpha, beta)
                val = game.blackAI.evaluate(best)
                if val > maxVal:
                    maxVal = val
                    bestBoard = best
                if maxVal > alpha:
                    alpha = maxVal
                if beta <= alpha:
                    break
            return bestBoard
        else:
            minVal = 10000
            bestBoard = game
            for b in self.derivedBoards(game):
                b.currentPlayer = 'B'
                best = self.minimax(b,depth + 1, alpha, beta)
                val = game.whiteAI.evaluate(best)
                if val < minVal:
                    minVal = val
                    bestBoard = best
                if minVal < beta:
                    beta = minVal
                if beta <= alpha:
                    break
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


