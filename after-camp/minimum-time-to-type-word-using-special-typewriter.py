class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        last = 'a'
        for c in word:
            dist = abs(ord(last)-ord(c))
            move = min(dist,26-dist) + 1
            time += move
            last = c
        print(ord('a'))
        return time