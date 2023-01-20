class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid) - 2
        n = len(grid) - 2
        max_matrix = [[0] * n  for _ in range(m)]
        max_elem = 0

        for i in range(n):
            for j in range(m):
                max_elem = 0
                for k in range(3):
                    tmp_max = max(grid[i+k][j:j+3])
                    if tmp_max > max_elem:
                        max_elem = tmp_max
                max_matrix[i][j] = max_elem
        return max_matrix

