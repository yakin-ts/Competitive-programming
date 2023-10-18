class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2!=0:
            return False
        answer = total//2
        mem = {}
        def solve(idx,target):
            if idx >=n:
                return False
            if target==answer:
                return True
            if (idx,target) in mem:
                return mem[(idx,target)]
            mem[(idx,target)] = solve(idx+1,target + nums[idx]) or solve(idx+1,target)

            return mem[(idx,target)]
        
        return solve(0,0)