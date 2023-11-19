class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i] + mat[i][n-1-i]
        ans -= mat[n//2][n//2] if n%2!=0 else 0
        return ans
        