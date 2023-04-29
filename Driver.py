from Heuristic import coinParity, cornersCaptured, mobility
from AIDriver import aiDriver
import time

def main():
    response = input("Type 'AI' for AI simulated Othello game, 'Human' for manual game: ")
    while response != 'AI' and response != 'Human':
        print("Error, invalid input, please enter either 'AI' or 'Human'")
        response = input("Type 'AI' for AI simulated Othello game, 'Human' for manual game: ")

    if response == 'AI':
        blackAI = None
        print("Choose black's AI")
        black = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'\nMobility -> 'Mobility'\n")
        while black != 'Coin' and black != 'Corner' and black != 'Mobility':
            print("Error, invalid input, please enter either 'Coin' or 'Corner'")
            black = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'\nMobility -> 'Mobility'\n")
        
        if black == 'Coin':
            blackAI = coinParity()
        elif black == 'Corner':
            blackAI = cornersCaptured()
        elif black == 'Mobility':
            blackAI = mobility()
        else:
            # Should never reach here, just in case sets to coinParity
            print("Error in selecting AI, automatically set black's AI to Coin Parity")
            blackAI = coinParity()
        
        whiteAI = None
        print("Choose white's AI")
        white = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'\nMobility -> 'Mobility'\n")
        while white != 'Coin' and white != 'Corner' and white != 'Mobility':
            print("Error, invalid input, please enter either 'Coin' or 'Corner'")
            white = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'\nMobility -> 'Mobility'\n")
        
        if white == 'Coin':
            whiteAI = coinParity()
        elif white == 'Corner':
            whiteAI = cornersCaptured()
        elif white == 'Mobility':
            whiteAI = mobility()
        else:
            # Should never reach here, just in case sets to coinParity
            print("Error in selecting AI, automatically set white's AI to Coin Parity")
            whiteAI = coinParity()

        max_depth = 4

        try:
            max_depth = int(input("Set max depth for minimax? (Default is 4): "))
            if (max_depth > 7):
                print(f"Depth of {max_depth} to large for Othello, using default of 4 instead")
                max_depth = 4
            if (max_depth < 1):
                print(f"Depth of {max_depth} to small for minimax, using default of 4")
        except Exception:
            print("Error, invalid input, defaulting to max depth of 4")
            max_depth = 4

        print(f"Black AI = {blackAI}")
        print(f"White AI = {whiteAI}")
        
        start = time.time()

        driver = aiDriver(blackAI=blackAI, whiteAI=whiteAI, MAX_DEPTH=max_depth)
        print(driver.run())
        print("Running...")

        end = time.time()
        print(f"runtime = {(end-start)}")
    else:
        #TODO: allow user to manually play game
        print("Selected manual Othello game")
        

main()