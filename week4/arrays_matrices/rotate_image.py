class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat_size = len(matrix)

        for i in range(mat_size//2):
            for j in range(i, mat_size -i -1):
                new_i = mat_size - i - 1
                new_j = mat_size - j - 1

                cur_elem = matrix[i][j]
                matrix[i][j] = matrix[new_j][i]
                matrix[new_j][i] = matrix[new_i][new_j]
                matrix[new_i][new_j] = matrix[j][new_i]
                matrix[j][new_i] = cur_elem