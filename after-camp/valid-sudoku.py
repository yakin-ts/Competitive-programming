class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        col_dict = {}

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cell_set = set()
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != '.':
                            if board[i + k][j + l] in cell_set or (i + k, board[i + k][j + l]) in row_dict or (j + l, board[i + k][j + l]) in col_dict:
                                return False
                            else:
                                cell_set.add(board[i + k][j + l])
                                row_dict[(i + k, board[i + k][j + l])] = 1
                                col_dict[(j + l, board[i + k][j + l])] = 1

        return True
