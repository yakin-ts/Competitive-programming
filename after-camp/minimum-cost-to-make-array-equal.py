class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)

        while mx > mn :
            md = mn + (mx-mn)//2
            cost1 , cost2 = 0,0

            for i in range(len(nums)):
                cost1+= abs(md - nums[i])*cost[i]
                cost2 += abs(md+1 - nums[i])*cost[i]
            if cost1 < cost2:
                mx = md
            else:
                mn = md+1
        res = 0 
        for j in range(len(nums)):
            res += abs(mn - nums[j])*cost[j]
        return res
        
        