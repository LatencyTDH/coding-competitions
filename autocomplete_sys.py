import collections
import heapq


class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = collections.defaultdict(TrieNode)  # prefix (str) -> TrieNode


class PatriciaTrie:
    def __init__(self):
        self.root = TrieNode()

    def add_item(self, item: str) -> None:
        node = self.root
        for char in item:
            node = node.children[char]
        node.is_terminal = True

    def find(self, query: str) -> list[str]:
        node = self.root
        for ch in query:
            if ch not in node.children:
                return []
            node = node.children[ch]

        return [query + suff for suff in self.dfs(node)]

    def dfs(self, start: TrieNode) -> list[str]:
        stack = [("", start)]
        seen = set()
        full_words = []

        while stack:
            word, node = stack.pop()
            seen.add(node)

            if node.is_terminal:
                full_words.append(word)

            for next_letter in node.children:
                if (node.children[next_letter]) not in seen:
                    stack.append((word + next_letter, node.children[next_letter]))

        return full_words


class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self.word_occ = collections.defaultdict(int)
        self.trie = PatriciaTrie()
        self.search_term = ""

        for i in range(len(sentences)):
            self.word_occ[sentences[i]] = times[i]
            self.trie.add_item(sentences[i])

    def input(self, c: str) -> list[str]:
        if c == "#":
            self.trie.add_item(self.search_term)
            self.word_occ[self.search_term] += 1
            self.search_term = ""
            return []

        self.search_term += c
        candidates = self.trie.find(self.search_term)
        counter = [(-self.word_occ[cand], cand) for cand in candidates]

        return [term for freq, term in heapq.nsmallest(3, counter)]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
if __name__ == "__main__":
    acs = AutocompleteSystem(
        ["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]
    )
    assert acs.input("i") == ["i love you", "island", "i love leetcode"]
    print("Query is 'i '\nSuggested sentences:", acs.input(" "))
    acs.input("d")
    acs.input("#")
    acs.input("i")
    acs.input("i")
    print("Typing in 'iid' should give me:", acs.input("d"))
