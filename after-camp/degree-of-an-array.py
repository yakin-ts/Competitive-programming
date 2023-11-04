class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start = {}
        end =  {}
        count = Counter(nums)

        for i,n in enumerate(nums):
            if n not in start:
                start[n]=i
                end[n]=i
            else:
                end[n] = i
        degree = len(nums)
        freq = max(count.values())
        for n in nums:
            if count[n]==freq:
                degree = min(degree,end[n]-start[n]+1)
        return degree

        