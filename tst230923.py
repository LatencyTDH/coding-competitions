from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.zero = Semaphore()
        self.even = Semaphore()
        self.odd = Semaphore()
    
    def next_num():
        self.i += 1
        if self.i > self.n:
            self.zero.release()
            self.even.release()
            self.odd.release()
        elif self.i % 2 == 0:
            self.even.release()
        else:
            self.odd.release()
        
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.zero.acquire()
            if self.i > self.n:
                break
            printNumber(0)
            self.next_num()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.even.acquire()
            if self.i > self.n:
                break
            printNumber(self.i)
            self.next_num()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.odd.acquire()
            if self.i > self.n:
                break
            printNumber(self.i)
            self.next_num()