class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        direction = [-1,0,1]
        for i in range(1, N):
            for j in range(N):
                min_ = float('inf')
                for x in direction:
                    if x+j < N and x+j >=0:
                        min_ = min(min_, matrix[i-1][j+x])
                matrix[i][j] += min_
        return min(matrix[-1])