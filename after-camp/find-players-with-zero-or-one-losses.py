class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost  = defaultdict(int)
        won = defaultdict(int)
        for x, y in matches:
            lost[y]+=1
            won[x]+=1
        ans = [[],[]]
        for key, val in lost.items():
            if val==1:
                ans[1].append(key)
        for key, val in won.items():
            if key not in lost:
                ans[0].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans

        