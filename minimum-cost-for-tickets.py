class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        mem = {}
        def dp(idx,day):
            if idx>=n:
                return 0
            if (idx,day) in mem:
                return mem[(idx,day)]
            if days[idx] > day:
                mem[(idx,day)] = min(dp(idx+1,days[idx])+costs[0],dp(idx+1,days[idx]+6)+costs[1],
                dp(idx+1,days[idx]+29)+costs[2])
            else:
                return dp(idx+1,day)
            return mem[(idx,day)]
        return dp(0,-1)