class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        mem = []
        for i in range(N):
            mem.append((ages[i],scores[i]))
        mem.sort()

        dp = [mem[i][1] for i in range(N)]
        ans = 0
        for i in range(N):
            scr = dp[i]
            for j in range(i):
                if scr >= mem[j][1]:
                    dp[i] = max(dp[i], dp[j] + scr)
            ans = max(ans,dp[i])
        return ans