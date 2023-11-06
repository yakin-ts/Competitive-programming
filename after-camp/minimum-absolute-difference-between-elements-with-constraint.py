from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        # bruteforce

        # diff = float('inf')
        # N = len(nums)
        # for i in range(N):
        #     for j in range(i,N-x):
        #         diff = min(diff,abs(nums[i]-nums[j+x]))
        # return diff

        def helper(items,target):
            if len(items)==1:
                return abs(items[0]-target)
            idx = bisect_left(items,target)
            if idx==0:
                return abs(items[0]-target)
            elif idx==len(items):
                return target - items[-1]
            else:
                idx-=1
                return min(abs(items[idx]-target),abs(items[idx+1]-target))
        items = SortedList()
        present = set()
        N = len(nums)
        start = 0
        diff= float('inf')
        for i in range(x,N):
            if nums[start] not in present:
                items.add(nums[start])
                present.add(nums[start])
            diff = min(diff,abs(helper(items,nums[i])))
            start+=1
        return diff
        


        