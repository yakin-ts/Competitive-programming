class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        right = len(nums) - 1


        while right >= left:
            mid = left + ((right - left)//2)

            if mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            elif mid < N - 1 and nums[mid+1] >  nums[mid]:
                left = mid + 1
            else:
                return mid

                 
        

        