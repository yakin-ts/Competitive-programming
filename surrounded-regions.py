class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        R = len(board)
        C = len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inbound(row, col):
            return 0 <= row < R and 0 <= col < C

        def dfs(row, col):
            if inbound(row, col) and board[row][col] == 'O':
                board[row][col] = 'Y'  

                for x, y in directions:
                    dfs(row + x, col + y)

        for i in range(R):
            if board[i][0] == 'O':
                dfs(i, 0)          
            if board[i][C - 1] == 'O':
                dfs(i, C - 1)    

        for j in range(C):
            if board[0][j] == 'O':
                dfs(0, j)           
            if board[R - 1][j] == 'O':
                dfs(R - 1, j)    

        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'