class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M =len(nums2)
        max_cross = 0
        mem = {}
        def dp(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            if i >= N or j >=M:
                return 0
            if nums1[i]==nums2[j]:
                return 1 + dp(i+1,j+1)
            else:
                mem[(i,j)]= max(dp(i+1,j),dp(i,j+1))
            
            return mem[(i,j)]
        return dp(0,0)