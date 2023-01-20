class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r= n-1

        for i in range(m):
            if target==matrix[i][l] or target==matrix[i][r]:
                return True
            elif target > matrix[i][l] and target < matrix[i][r]:
                while r >= l:
                    mid = (r+l)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid] > target:
                        r = mid-1
                    elif matrix[i][mid] < target:
                        l = mid+1
        return False