class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N = len(s)
        mem = defaultdict(int)
        for i in range(N-9):
            mem[s[i:i+10]] +=1
        ans = []
        for key, val in mem.items():
            if val > 1:
                ans.append(key)
        return ans
