class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, nums: List[int]) -> int:
        nums.sort()
        nums[0] = 1
        for i in range(len(nums)-1):
            if abs(nums[i]- nums[i+1]) > 1:
                nums[i+1] = nums[i] + 1
        return nums[-1]