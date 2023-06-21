class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        buy_trans = [0 for _ in range(N)]
        buy_trans[0] = -prices[0]
        sell_trans = [0]*N

        for i in range(1,N):
            buy_trans[i] = max(buy_trans[i-1],sell_trans[i-1] - prices[i])
            sell_trans[i] = max(sell_trans[i-1],buy_trans[i-1] + prices[i] - fee)
        return sell_trans[-1]