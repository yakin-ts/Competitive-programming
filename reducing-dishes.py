class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        N = len(satisfaction)
        mem = {}
        def dp(idx,times):
            if idx >= N:
                return 0
            if (idx,times) in mem:
                return mem[(idx,times)]
            take = satisfaction[idx]*times + dp(idx+1,times+1)
            remove = 0 + dp(idx+1,times)
            mem[(idx,times)] = max(take,remove)

            return mem[(idx,times)]
        
        return dp(0,1)