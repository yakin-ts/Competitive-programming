class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            gcd = nums[i]
            for j in range(i, len(nums)):
                gcd = math.gcd(gcd, nums[j])
                if gcd == k:
                    count += 1
        return count