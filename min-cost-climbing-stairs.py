class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        n = len(cost)
        def DP(n):
            if n==0 or n==1:
                return cost[n]
            if n in mem:
                return mem[n]
            if n not in mem:
                mem[n] = cost[n] + min(DP(n-1),DP(n-2))
            return mem[n]
        
        return min(DP(n-1),DP(n-2))