class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        mem = defaultdict(int)

        def dp(i,target):
            if i >= N or target <=0:
                return target==0
            state = (i,target)
            if state not in mem:
                mem[state] = dp(i+1,target-nums[i]) or dp(i+1,target)
            return mem[state]
        
        return sum(nums)%2==0 and dp(0,sum(nums)//2)