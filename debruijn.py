from collections import deque

def crackSafe(n: int, k: int) -> str:
        if n == 1:
            return "".join(map(str, range(k)))
        if k == 1:
            return "0" * n
        first = "0" * (n-1)
        stack = [(first)]
        res = deque([])
        visited = set([])
        v = first
        
        while stack:
            add_some = False
            for n in map(str, range(k)):
                neigh = v + n
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(v)
                    v = neigh[1:]
                    add_some = True
            if not add_some:
                res.append(v[0])
                v = stack.pop()
        return v[1:] + "".join(res)

if __name__ == '__main__':
    print(crackSafe(2, 4))