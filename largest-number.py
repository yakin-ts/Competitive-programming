class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def concatenate(num):
            if num == 0:
                return '0'
            num_str = str(num)
            return num_str * (10 // len(num_str) + 1)
        
        nums = sorted(nums, key=lambda x: concatenate(x), reverse=True)
        if nums[0] == 0:
            return '0'
        
        return ''.join(map(str, nums))