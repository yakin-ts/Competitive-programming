class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = {}
        
        def dp(row, col):
            if row == 0 and col == 0:
                return poured
            if row < 0 or col < 0 or col > row:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            left = dp(row - 1, col - 1)
            right = dp(row - 1, col)
            memo[(row, col)] = max((left - 1) / 2, 0) + max((right - 1) / 2, 0)
            return memo[(row, col)]
        
        dp(query_row, query_glass)
        return min(memo[(query_row, query_glass)], 1) if ((query_row, query_glass)) in memo else min(1, poured)