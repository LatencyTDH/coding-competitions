from typing import List
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing.pool import Pool
import concurrent.futures
import random
from copy import deepcopy
import time
import os

ACTIVE = 1
INACTIVE = 0
ACTIVE_TO_INACTIVE = -1
INACTIVE_TO_ACTIVE = 2

def gameOfLife_st(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    
    for i in range(m):
        for j in range(n):
            active_neighs = total_active_neighbors(board, i, j, m, n)
            if board[i][j] == ACTIVE:
                if active_neighs < 2 or active_neighs > 3:
                    board[i][j] = ACTIVE_TO_INACTIVE
            elif active_neighs == 3:
                board[i][j] = INACTIVE_TO_ACTIVE
    
    postprocess(board, m, n)

def gameOfLife(board: List[List[int]], pool, cpus=4) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    splits = [(i, j, m, n) for i in range(m) for j in range(n)]
    futures = pool.map(_gameOfLife, splits, chunksize=(m * n) // cpus)
    for fut in futures:
        ij, action = fut
        i, j = ij
        board[i][j] = action
    postprocess(board, m, n)
    # futures = { pool.submit(adjust_square, board, i, j) for i in range(m) for j in range(n) }
    # wait(futures)

def wait(futures):
    for fut in concurrent.futures.as_completed(futures):
        fut.result()

def _gameOfLife(tup) -> None:
    i, j, m, n = tup
    """
    Do not return anything, modify board in-place instead.
    """
    active_neighs = total_active_neighbors(board, i, j, m, n)
    if board[i][j] == ACTIVE:
        if active_neighs < 2 or active_neighs > 3:
            return ((i, j), ACTIVE_TO_INACTIVE)
    elif active_neighs == 3:
        return ((i, j), INACTIVE_TO_ACTIVE)  
    return ((i, j), board[i][j])      

def total_active_neighbors(board, i, j, m, n):
    dirs = ((-1,-1), (-1,0), (-1,1), (0, -1), (0, 1), (1,-1), (1,0), (1,1))
    total = 0
    for dr, dc in dirs:
        r, c = i + dr, j + dc
        if (0 <= r < m and 0 <= c < n 
            and (board[r][c] == ACTIVE or board[r][c] == ACTIVE_TO_INACTIVE)):
            total += 1
    return total

def adjust_square(board, i, j):
    if board[i][j] == ACTIVE_TO_INACTIVE:
        board[i][j] = INACTIVE
    elif board[i][j] == INACTIVE_TO_ACTIVE:
        board[i][j] = ACTIVE

def postprocess(board, m, n):
    for i in range(m):
        for j in range(n):
            if board[i][j] == ACTIVE_TO_INACTIVE:
                board[i][j] = INACTIVE
            elif board[i][j] == INACTIVE_TO_ACTIVE:
                board[i][j] = ACTIVE

def test_case_1():
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    gameOfLife(board)
    assert board == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

n = 1000
board = [[random.choice([0,1]) for i in range(n)] for j in range(n)]

if __name__ == '__main__':
    ncpus = os.cpu_count()
    board2 = deepcopy(board)
    print("Exceucting parallel game of life...")
    with ProcessPoolExecutor() as pool:
        start = time.monotonic()
        gameOfLife(board, pool, cpus=64)
        elapsed = time.monotonic() - start
        print(f"Time to complete game was {elapsed} secs.")
    start = time.monotonic()
    gameOfLife_st(board2)
    elapsed2 = time.monotonic() - start
    print(f"Time to single-threaded game was {elapsed2} secs.")
    
    print("Parallel improvement: t_s / t_p =", round(elapsed2 / elapsed, 3))
    # assert board == board2
    