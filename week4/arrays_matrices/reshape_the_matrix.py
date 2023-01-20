class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_size = len(mat)*len(mat[0])

        if (r > mat_size or c > mat_size) or r*c != mat_size:
            return mat
        
        row = r
        col = mat_size//row
        reshaped = [[0]*col for _ in range(row)]
        count = 0

        for r, row in enumerate(mat):
            for c, elem in enumerate(row):
                i = (count)//col
                j = count%col
                reshaped[i][j] = mat[r][c]
                count +=1
                
        return reshaped




        