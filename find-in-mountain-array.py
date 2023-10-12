# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        N = arr.length()
        start = 0
        end = N-1

        
        while end > start:
            peak = start + (end-start)//2
            mid_val = arr.get(peak)
            mid_plus = arr.get(peak+1)
            mid_minus = arr.get(peak-1)

            if mid_val > mid_minus and mid_val>mid_plus:
                break
            elif mid_val > mid_minus:
                start = peak
            else:
                end = peak

        if target==mid_val:
            return peak
        if target > mid_val:
            return -1
        
        # check on the increasing section
        left = 0
        right = peak
    #   [1,2]
        while right > left:
            mid = left + (right-left)//2
            val = arr.get(mid)

            if val==target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid
        
        left = peak
        right =  N-1

        while right >  left:
            mid = left + (right-left)//2
            val = arr.get(mid)
            if val==target:
                return mid
            elif val < target:
                right = mid
            else:
                left = mid+1
        ans = arr.get(left)
        return -1 if ans!= target else left