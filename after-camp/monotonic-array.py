class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        N = len(nums)
        if N==1:
            return True
        start = 0
        end = 1
        while end < N and nums[start]==nums[end]:
            end+=1
        if end < N and nums[0] > nums[end]:
            for i in range(end,N):
                if nums[i] > nums[i-1]:
                    return False
        elif end < N:
            for i in range(end,N):
                if nums[i] < nums[i-1]:
                    return False
        return True
        

        