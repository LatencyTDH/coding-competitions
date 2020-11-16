from collections import defaultdict
import heapq
from typing import List


class TrieNode(object):
    def __init__(self):
        self.is_terminal = False
        self.children = defaultdict(TrieNode)  # prefix (str) -> TrieNode


class PatriciaTrie(object):
    def __init__(self):
        self.root = TrieNode()

    def add_item(self, item):
        node = self.root
        for char in item:
            node = node.children[char]
        node.is_terminal = True

    def find(self, query):
        node = self.root
        result = [""]
        for ch in query:
            if ch not in node.children:
                return []
            else:
                result.append(ch)
                node = node.children[ch]

        prefixed = "".join(result)
        if node:
            return [prefixed + suff for suff in self.dfs(node)]
        else:
            return [prefixed]

    def dfs(start):
        stack = [("", start)]
        visited = set([])
        full_words = []
        while stack:
            word, node = stack.pop()
            if not node.children or node.is_terminal:
                full_words.append(word)
            for key in node.children:
                if node.children[key] not in visited:
                    stack.append((word + key, node.children[key]))
            visited.add(node)
        return full_words


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.word_occ = defaultdict(int)
        self.trie = PatriciaTrie()
        self.search_term = ""
        for s, t in zip(sentences, times):
            self.word_occ[s] = t
            self.trie.add_item(s)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.add_item(self.search_term)
            self.word_occ[self.search_term] += 1
            self.search_term = ""
            return []
        else:
            self.search_term += c
        candidates = self.trie.find(self.search_term)
        counter = [(-self.word_occ[cand], cand) for cand in candidates]
        heapq.heapify(counter)
        hotlist = []
        for i in range(3):
            if counter:
                _, hotsent = heapq.heappop(counter)
                hotlist.append(hotsent)
        return hotlist


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
if __name__ == '__main__':
    acs = AutocompleteSystem(
        ["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
    assert acs.input('i') == ["i love you", "island", "i love leetcode"]
    print("Query is 'i '\nSuggested sentences:", acs.input(' '))
    acs.input('d')
    acs.input('#')
    acs.input('i')
    acs.input('i')
    print("Typing in 'iid' should give me:", acs.input('d'))
