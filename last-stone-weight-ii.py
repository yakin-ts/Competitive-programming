class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        mem = {}
        def solve(count,take,dont_take):
            if count==len(stones):
                return abs(take - dont_take)
            if (take,dont_take) in mem:
                return mem[(take,dont_take)]
            take_sum = solve(count+1,take + stones[count],dont_take)
            dont_take_sum  = solve(count+1,take,dont_take + stones[count])
            mem[(take,dont_take)] = min(take_sum,dont_take_sum)

            return mem[(take,dont_take)]
        
        return solve(0,0,0)