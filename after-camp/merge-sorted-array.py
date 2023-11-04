class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m-1
        right = n - 1
        ptr = n + m -1

        while right >= 0 and left>=0:
            if nums2[right] >= nums1[left]:
                nums1[ptr] = nums2[right]
                right -=1
                
            else:
                nums1[ptr] = nums1[left]
                left -=1
            ptr -=1
        nums1[:right+1] = nums2[:right+1]
