class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur  = cur.children[idx]
        cur.is_end = True

    def longestWord(self, words: List[str]) -> str:
        root = self.root
        self.longest = ''

        for word in words:
            self.insert(word)

        def dfs(cur,wrd):
            if not cur or  (cur is not root and not cur.is_end):
                return
            for i in range(26):
                if cur.children[i] and  cur.children[i].is_end:
                    ch = ord('a') + i
                    if len(wrd + chr(ch)) > len(self.longest):
                        self.longest = wrd + chr(ch)
                    dfs(cur.children[i],wrd + chr(ch))
        dfs(self.root,"")

        return self.longest