class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = -inf

        for i,n in enumerate(nums):
            if i!=0:
                nums[i] += nums[i-1]
            ans = max(ans,ceil(nums[i]/(i+1)))
        return ans