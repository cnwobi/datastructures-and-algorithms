from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.end_of_word = True

    def contains(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end_of_word


def findSubstrings(words, parts):
    result = []
    trie = Trie()
    for part in parts:
        trie.insert(part)

    for word in words:
        curr = [0, -1]
        for i in range(len(word)):
            for j in reversed(range(len(word))):
                if trie.contains(word[i:j + 1]):
                    curr = max(curr, [i, j], key=lambda x: x[1] - x[0])
        i, j = curr
        result.append(f"{word[0:i]}[{word[i:j + 1]}]{word[j + 1:]}" if j != -1 else word)
    return result


if __name__ == '__main__':
    words = ["Apple", "Melon", "Orange", "Watermelon"]
    parts = ["a", "mel", "lon", "el", "An"]

    print(findSubstrings(words, parts))
