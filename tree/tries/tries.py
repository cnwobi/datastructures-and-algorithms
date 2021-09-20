from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

    def __repr__(self):
        return f" \n children -> {self.children} end_of_word -> {self.end_of_word}"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_words(self,words):
        for word in words:
            self.insert(word)

    def insert(self, word):
        current: TrieNode = self.root
        for ch in word:
            current = current.children[ch]
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for ch in word:
            if not (ch in current.children):
                return False
            current = current.children[ch]
        return current.end_of_word

    def is_prefix(self, word):
        current = self.root
        for ch in word:
            if not (ch in current.children):
                return False
            current = current.children[ch]
        return True

    def __repr__(self):
        return f"f -> {self.root}"


if __name__ == '__main__':
    trie = Trie()

    words = ["Apple", "Melon", "Orange", "Watermelon"]
    parts = ["a", "mel", "lon", "el", "An"]
    trie.insert_words(parts)

    for word in words:
        result = []
        prefix = ""
        for ch in word:
            if trie.is_prefix(curr + ch ):
                result.append()





