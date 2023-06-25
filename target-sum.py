class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        N = len(nums)
        mem = {}

        def sum_along(idx, run_sum):
            if idx >= N:
                return 1 if target == run_sum else 0

            if (idx, run_sum) in mem:
                return mem[(idx, run_sum)]

            add = sum_along(idx + 1, run_sum + nums[idx])
            sub = sum_along(idx + 1, run_sum - nums[idx])

            mem[(idx, run_sum)] = add + sub
            return mem[(idx, run_sum)]

        return sum_along(0, 0)