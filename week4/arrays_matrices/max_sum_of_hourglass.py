class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 2
        n = len(grid[0]) -2
        max_sum = 0
        tmp_sum = 0

        for i in range(m):
            for j in range(n):
                tmp_sum = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
                max_sum = max(max_sum, tmp_sum)

        return max_sum