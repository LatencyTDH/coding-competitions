import random

def knightProbability(N: int, K: int, r: int, c: int) -> float:
    n_sims = int(1e6)
    total = 0
    for i in range(n_sims):
        total += simulate(N, K, r, c)
    return total / n_sims

def simulate(N, K, r, c):
    dirs = [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for i in range(K):
        dr, dc = random.sample(dirs, 1)[0]
        r += dr
        c += dc
        if not within_board(N, r, c):
            return 0
    return 1
        

def within_board(N, x, y):
    return 0 <= x < N and 0 <= y < N

if __name__ == '__main__':
    print(knightProbability(3, 2, 0, 0))
    