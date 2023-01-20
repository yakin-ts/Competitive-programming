class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """

        Do not return anything, modify nums1 in-place instead.
        """
        l=m-1
        r=n-1
        while r>(m-1):
            if nums2[r] > nums1[m+l]:
                nums1[m+r] = nums2[r]
                r-=1
            elif nums2[r]==nums1[m+l]:
                l+=1
                nums1[m+l]==nums2[r]
                r-=1
            else:
                nums1[m+l+1] = nums1[m+l]
                nums1[m+l] = nums2[r]
                l+=1