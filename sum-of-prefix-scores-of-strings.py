class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.val = 1
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert(word)
        ans = []
        for word in words:
            ans.append(self.sum(word))
        return ans
    def insert(self,word):
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            else:
                cur.children[idx].val += 1
            cur = cur.children[idx]
    def sum(self,word):
        cur= self.root
        tot = 0
        for ch in word:
            idx = ord(ch) - ord('a')
            cur = cur.children[idx]
            tot += cur.val
        return tot