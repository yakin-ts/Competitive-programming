class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        _min = nums[0]

        for n in nums:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and stack[-1][1] < n:
                return True
            stack.append((n,_min))
            _min = min(_min,n)
        return False