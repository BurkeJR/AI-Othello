from AIDriver import aiDriver
from Heuristic import coinParity, cornersCaptured, mobility, stability, combination
import time

def main():
    bAI = [coinParity(), cornersCaptured(), mobility(), stability()]
    wAI = [combination()]
    results = [['' for _ in range(1)] for _ in range(4)]

    start = time.time()

    for i in range(len(bAI)):
        for j in range(len(wAI)):
            blackAI = bAI[i]
            whiteAI = wAI[j]
            driver = aiDriver(blackAI, whiteAI, MAX_DEPTH=5, wordy=False)
            results[i][j] = driver.run()
    end = time.time()
    print(results)
    print(f"Runtime = {end - start}")









if __name__ == '__main__':
    main()