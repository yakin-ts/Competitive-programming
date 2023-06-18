class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<2:
            return n

        dp = [1 for _ in range(n+1)]
        dp[0] = 0 
    
        def helper(idx):
            if idx > ceil(n//2):
                return
            if 2*idx <= n:
                dp[2*idx] = dp[idx]
            if 2*idx + 1 <= n:
                dp[2*idx+1] = dp[idx] + dp[idx+1]
            return helper(idx+1)

        helper(0)
        return max(dp)