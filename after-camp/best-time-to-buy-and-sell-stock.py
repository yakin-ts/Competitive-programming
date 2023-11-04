class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit  = 0 
        N = len(prices)
        for i in range(1,N):
            if buy > prices[i]:
                buy = prices[i]
            if profit < (prices[i] - buy):
                profit = prices[i] - buy
        return profit


        