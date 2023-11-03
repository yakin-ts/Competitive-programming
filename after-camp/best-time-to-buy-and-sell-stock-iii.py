class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(idx, buy, tx):
            if tx == 0 or idx == N:
                return 0

            if dp[idx][buy][tx] != -1:
                return dp[idx][buy][tx]

            if buy:
                profit = max(-prices[idx] + solve(idx + 1, 0, tx),
                             solve(idx + 1, 1, tx))
            else:
                profit = max(prices[idx] + solve(idx + 1, 1, tx - 1),
                             solve(idx + 1, 0, tx))

            dp[idx][buy][tx] = profit
            return dp[idx][buy][tx]

        N = len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N)]

        return solve(0, 1, 2)
