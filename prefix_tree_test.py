from trie import Trie
from big_words import DICTIONARY

def search(tree: Trie, prefix: str, limit=None):
	found_words = []
	def _search(node, buffer):
		if limit and len(found_words) >= limit:
			return
		if node.is_word:				
			found_words.append("".join(buffer[:]))
		
		for ch in node.children:
			buffer.append(ch)
			_search(node.children[ch], buffer)
			buffer.pop()

	start = tree.root
	for ch in prefix:
		if ch in start.children:
			start = start.children[ch]
		else:
			return found_words
	
	buffer = [prefix]
	_search(start, buffer)
	return found_words

if __name__ == "__main__":
	words = DICTIONARY
	tree = Trie()
	for word in words:
		tree.insert(word)

	print(search(tree, "hand"))
