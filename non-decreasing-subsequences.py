class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)
        res = []
        def helper(start,arr):
            nonlocal res
            if start >= N:
                return
            if arr and arr[-1] > nums[start]:
                helper(start+1,arr)
            else:
                arr.append(nums[start])
                if len(arr)>1 and arr not in res:
                    res.append(arr.copy())
                helper(start+1, arr)
                arr.pop()
                helper(start+1,arr)
        helper(0,[])

        return res