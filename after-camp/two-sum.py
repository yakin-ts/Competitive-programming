class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        ans = [0,0]
        for i,n in enumerate(nums):
            if target - n in mem:
                ans = [i,mem[target-n]]
                break
            mem[n]=i
        return ans


        