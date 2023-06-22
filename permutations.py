class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results = []

        def backtrack(nums, current):
            if len(current) == len(nums):
                results.append(current[:])
            else:
                for i in range(len(nums)):
                    if nums[i] in current:
                        continue
                    current.append(nums[i])
                    backtrack(nums, current)
                    current.pop()

        backtrack(nums, [])
        return results