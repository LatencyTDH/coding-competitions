import sys

def isqrt(num):
    x = num // 2 if num > 2 else 1
    decreased = False
    while True:
        nx = (x + num // x) // 2
        if x == nx or (decreased and nx > x):
            break
        decreased = nx < x
        x = nx
    
    return x
            

if __name__ == '__main__':
	print(isqrt(32333))