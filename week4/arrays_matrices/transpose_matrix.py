class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        transpose = [ [0]*m for _ in range(n)]

        for row in range(len(transpose)):
            for col in range(len(transpose[0])):
                transpose[row][col] = matrix[col][row]
        
        return transpose