class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        res = ''
        w1 = len(word1)
        w2 = len(word2)
        while p1 < w1 and p2 < w2:
            res += word1[p1]
            p1+=1
            res += word2[p2]
            p2+=1

        if p1 < w1:
            res += word1[p1:]
        if p2 < w2:
            res += word2[p2:]
        
        return res