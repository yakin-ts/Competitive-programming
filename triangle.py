class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        L = len(triangle)
        dp = triangle[-1]
        
        for i in range(L-2, -1, -1):
            for j,elem in enumerate(triangle[i]):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]

        return dp[0]