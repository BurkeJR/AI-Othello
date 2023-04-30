from AIDriver import aiDriver
from Heuristic import coinParity, cornersCaptured, mobility, stability
import time

def main():
    bAI = [coinParity(), cornersCaptured(), mobility(), stability()]
    wAI = [coinParity(), cornersCaptured(), mobility(), stability()]
    results = [['' for _ in range(5)] for _ in range(5)]
    results[0] = ['', str(wAI[0]), str(wAI[1]), str(wAI[2]), str(wAI[3])]
    results[1][0] = str(bAI[0])
    results[2][0] = str(bAI[1])
    results[3][0] = str(bAI[2])
    results[4][0] = str(bAI[3])

    start = time.time()

    for i in range(len(bAI)):
        for j in range(len(wAI)):
            blackAI = bAI[i]
            whiteAI = wAI[j]
            driver = aiDriver(blackAI, whiteAI, MAX_DEPTH=5, wordy=False)
            results[i+1][j+1] = driver.run()
    end = time.time()
    print(results)
    print(f"Runtime = {end - start}")









if __name__ == '__main__':
    main()