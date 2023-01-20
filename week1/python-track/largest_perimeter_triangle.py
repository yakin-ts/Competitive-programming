class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largestPerimeter = 0
        leng = len(nums)

        nums.sort()
        
        for i in range(leng-3,-1,-1):
            if nums[i] + nums[i+1] > nums[i+2]:
                largestPerimeter = nums[i] + nums[i+1] + nums[i+2]
                break

        return largestPerimeter