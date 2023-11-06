class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        
        if N <= 1:
            return
        left = N-2
        right = N-1
        while left >=0:
            if nums[left] <nums[right]:
                break
            left-=1
            right-=1
        else:
            nums.reverse()
            return
        right = N-1
        while right > left:
            if nums[right] > nums[left]:
                break
            right -=1
        
        nums[left], nums[right] = nums[right], nums[left]
        
        nums[left + 1:] = reversed(nums[left + 1:])
