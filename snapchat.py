# Each line in the following data represents a friendship on snapchat. The third column specifies the quality of the relationship. 'f' for just a friend and 'bf' for best friend.

# ashley,isabella,f
# nick,josh,f
# josh,mike,bf
# jane,josh,f
# mike,dan,bf

# Given this dataset, write a program to recommend friends to nick.

# ashley -> no friends
# graph : adjacency list: friend name -> set(immediate friends)
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

friend_pairs = [
	('a', 'b', 'bf'),
	('b', 'c', 'bf'),
	('c', 'a', 'bf')
]

# josh -> mike (bf) -> dan
#         josh -> jane -> karen
# nick - josh josh - mike mike - dan
# A -> B (bf) -> C (bf) -> K
# A -> D (f) -> J
# (dist, -best_friend)

def compute_adjacency_list(data):
    adj = defaultdict(set)
    quality = {} # (friend1, friend2) -> 'f' or 'bf'
    for start, end, relationship in data:
        adj[start].add(end)
        adj[end].add(start)
        quality[(start, end)] = relationship == 'bf'
    
    return adj, quality 
        

def find_mutual_friends(graph, bf_relationships, person, friend_limit):
    frontier = [(0, 0, person)]
    visited = set()
    active_set = set([person])
    mutual_friends = []
    
    while frontier:
        dist, is_bf, friend = heappop(frontier)
        visited.add(friend)
        active_set.remove(friend)
        
        if friend_limit > 0:
            if dist > 1:
                mutual_friends.append(friend)
                friend_limit -= 1
        else:
            return mutual_friends
        
        for neighbor in graph[friend]:
            if neighbor not in visited and neighbor not in active_set:
                is_bf = (
                    bf_relationships.get((friend, neighbor), 0) | bf_relationships.get((neighbor, friend), 0)
                )
                heappush(frontier, (dist + 1, -is_bf, neighbor))
                active_set.add(neighbor)
        
    return mutual_friends

if __name__ == "__main__":
    friend_graph, quality_graph = compute_adjacency_list(friend_pairs)
    friends = find_mutual_friends(friend_graph, quality_graph, 'a', 1)
    print(friends)
    