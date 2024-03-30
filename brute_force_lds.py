import math

def has_lds_of_size_k(start, k, largest, seq): 
    if k == 0: return True 
    for j in range(start, len(seq)): 
     if seq[j] < largest: 
        old = largest 
        largest = seq[j] 
        if has_lds_of_size_k(j + 1, k - 1, largest, seq):
            return True 
        largest = old
    return False


def lds(arr): 
    if not arr: return 0 
    largest = 1 
    for size in range(2, len(arr) + 1): 
      if has_lds_of_size_k(0, size, math.inf, arr): 
          largest = max(largest, size) 
    return largest

if __name__ == '__main__':
    print(lds([4,1,3,5,2])) # 3
    print(lds([4,3,2,1])) # 4
    print(lds([1,2,3,4,5])) # 1
    print(lds([1,12,7,0,10])) # 3
    print(lds([1,2,5,4,10])) # 2
    print(lds([3,2,1,1000,999,888,777,666,0]))