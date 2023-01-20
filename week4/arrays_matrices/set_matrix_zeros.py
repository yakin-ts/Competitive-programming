class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_row = {}
        zeros_col = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    zeros_row[i] = 1
                    zeros_col[j] = 1
        
        for i in range(len(matrix)):
            if i in zeros_row:
                matrix[i] = [0]*len(matrix[0])
                continue
            for j in range(len(matrix[i])):
                if j in zeros_col:
                    matrix[i][j] = 0
            