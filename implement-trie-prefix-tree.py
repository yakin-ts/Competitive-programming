class TrieNode:
    def __init__(self):
        self.isWordEnd = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for chr in word:
            idx = ord(chr) -ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isWordEnd = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for chr in word:
            idx = ord(chr) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]

        return cur.isWordEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for chr in prefix:
            idx = ord(chr) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]

        return True 

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)