from functools import cache

def findCheese(self, master: 'GridMaster') -> int:
        _DIRECTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        seen = set()

        def move_back(direction: str) -> None:
            if direction == 'D':
                master.move('U')
            elif direction == 'L':
                master.move('R')
            elif direction == 'R':
                master.move('L')
            elif direction == 'U':
                master.move('D')

        @cache
        def search(pos: tuple[int, int]):
            if master.isTarget():
                return 0
            seen.add(pos)
            print("exploring", pos)

            for d in _DIRECTIONS:
                dr, dc = _DIRECTIONS[d]
                new_pos = pos[0] + dr, pos[1] + dc
                if master.canMove(d) and new_pos not in seen:
                    move_cost = master.move(d)
                    cost = search(new_pos)
                    if cost != -1:
                        return move_cost + cost
                    move_back(d)
                    seen.remove(new_pos)
            
            seen.remove(pos)
            return -1
        return search((0, 0))