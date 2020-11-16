from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.work = Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.n):
            if i % 3 == 0 and i % 5 != 0:
                printFizz()
                self.work.notify_all()
            else:
                self.do_wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n):
            if i % 5 == 0 and i % 3 != 0:
                printBuzz()
                self.work.notify_all()
            else:
                self.do_wait()
             
    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n):
            if i % 5 == 0 and i % 3 == 0:
                printFizzBuzz()
                self.work.notify_all()
            else:
                self.do_wait()
            

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if i % 5 != 0 and i % 3 != 0:
                printNumber(i)
                self.work.notify_all()
            else:
                self.do_wait()
    
    def do_wait(self):
        with self.work:
            self.work.wait()