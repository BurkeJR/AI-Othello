from Heuristic import coinParity, cornersCaptured, mobility, stability, combination
from AIDriver import aiDriver
from PlayerDriver import player
import time

def main():
    response = input("Type 'AI' for AI simulated Othello game, 'Human' for manual game: ")
    while response != 'AI' and response != 'Human':
        print("Error, invalid input, please enter either 'AI' or 'Human'")
        response = input("Type 'AI' for AI simulated Othello game, 'Human' for manual game: ")

    if response == 'AI':
        blackAI = None
        print("\nChoose black's AI")
        black = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'\nMobility -> 'Mobility'\nStability -> 'Stability'\nCombination -> 'Combination'\n")
        while black != 'Coin' and black != 'Corner' and black != 'Mobility' and black != 'Stability' and black != 'Combination':
            print("\nError, invalid input, please enter either 'Coin', 'Corner', 'Mobility', 'Stability' or 'Combination'")
            black = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'\nMobility -> 'Mobility'\nStability -> 'Stability'\nCombination -> 'Combination'\n")
        
        if black == 'Coin':
            blackAI = coinParity()
        elif black == 'Corner':
            blackAI = cornersCaptured()
        elif black == 'Mobility':
            blackAI = mobility()
        elif black == 'Stability':
            blackAI = stability()
        elif black == 'Combination':
            blackAI = combination()
        else:
            # Should never reach here, just in case sets to coinParity
            print("\nError in selecting AI, automatically set black's AI to Coin Parity")
            blackAI = coinParity()
        
        whiteAI = None
        print("\nChoose white's AI")
        white = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'\nMobility -> 'Mobility'\nStability -> 'Stability'\nCombination -> 'Combination'\n")
        while white != 'Coin' and white != 'Corner' and white != 'Mobility' and white != 'Stability' and white != 'Combination':
            print("\nError, invalid input, please enter either 'Coin', 'Corner', 'Mobility', 'Stability' or 'Combination'")
            white = input("Coin Parity -> 'Coin'\nCorners Captured -> 'Corner'\nMobility -> 'Mobility'\nStability -> 'Stability'\nCombination -> 'Combination'\n")
        
        if white == 'Coin':
            whiteAI = coinParity()
        elif white == 'Corner':
            whiteAI = cornersCaptured()
        elif white == 'Mobility':
            whiteAI = mobility()
        elif white == 'Stability':
            whiteAI = stability()
        elif white == 'Combination':
            whiteAI = combination()
        else:
            # Should never reach here, just in case sets to coinParity
            print("Error in selecting AI, automatically set white's AI to Coin Parity")
            whiteAI = coinParity()

        max_depth = 5

        try:
            max_depth = int(input("\nSet max depth for minimax? (Default is 5): "))
            if (max_depth > 7):
                print(f"Depth of {max_depth} to large for Othello, using default of 5 instead")
                max_depth = 5
            if (max_depth < 1):
                print(f"Depth of {max_depth} to small for minimax, using default of 5")
        except Exception:
            print("Error, invalid input, defaulting to max depth of 6")
            max_depth = 5

        print(f"\nBlack AI = {blackAI}")
        print(f"White AI = {whiteAI}")
        
        start = time.time()

        driver = aiDriver(blackAI=blackAI, whiteAI=whiteAI, MAX_DEPTH=max_depth)
        print("Running...")
        print(driver.run())
        

        end = time.time()
        print(f"runtime = {(end-start)}")
    else:
        driver = player()
        print(driver.run())
        

main()