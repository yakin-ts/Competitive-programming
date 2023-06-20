class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mem = {}
        for num in arr:
            if num - difference in mem:
                mem[num] = mem[num - difference] + 1
            else:
                mem[num] = 1
        ans = max(mem.values())

        return ans