class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)

        def helper(nums):
            n = len(nums)
            dp = [0] * (n + 1)
            dp[1] = nums[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            return dp[n]
        
        return max(helper(nums[1:]), helper(nums[:-1]))