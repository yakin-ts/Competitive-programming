class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if m==1 and n==1:
            return matrix[0][0]==target
        for idx in range(m):
            left = 0
            right = n - 1
            if matrix[idx][0] > target:
                break
            while right >= left:
                mid = left + (right - left)//2

                if matrix[idx][mid]==target:
                    return True
                elif matrix[idx][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

        