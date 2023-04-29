from Heuristic import coinParity, cornersCaptured
from AIDriver import aiDriver

def main():
    response = input("Type 'AI' for AI simulated Othello game, 'Human' for manual game: ")
    while response != 'AI' and response != 'Human':
        print("Error, invalid input, please enter either 'AI' or 'Human'")
        response = input("Type 'AI' for AI simulated Othello game, 'Human' for manual game: ")

    if response == 'AI':
        blackAI = None
        print("Choose black's AI")
        black = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'")
        while black != 'Coin' and black != 'Corner':
            print("Error, invalid input, please enter either 'Coin' or 'Corner'")
            black = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'")
        
        if black == 'Coin':
            blackAI = coinParity()
        elif black == 'Corner':
            blackAI = cornersCaptured()
        else:
            # Should never reach here, just in case sets to coinParity
            print("Error in selecting AI, automatically set black's AI to Coin Parity")
            blackAI = coinParity()
        
        whiteAI = None
        print("Choose white's AI")
        white = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'")
        while white != 'Coin' and white != 'Corner':
            print("Error, invalid input, please enter either 'Coin' or 'Corner'")
            white = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'")
        
        if white == 'Coin':
            whiteAI = coinParity()
        elif white == 'Corner':
            whiteAI = cornersCaptured()
        else:
            # Should never reach here, just in case sets to coinParity
            print("Error in selecting AI, automatically set white's AI to Coin Parity")
            whiteAI = coinParity()

        driver = aiDriver(blackAI=blackAI, whiteAI=whiteAI)
        print(driver.run())
    else:
        #TODO: allow user to manually play game
        print("Selected manual Othello game")
        


    
    

    



main()