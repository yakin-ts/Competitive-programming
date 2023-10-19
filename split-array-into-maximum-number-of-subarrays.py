class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        cur = 0
        sub_count = 0
        for i in range(len(nums)):
            if cur==0:
                cur = nums[i]
            else:
                cur &= nums[i]
            if cur==0:
                sub_count +=1
        return max(1,sub_count)