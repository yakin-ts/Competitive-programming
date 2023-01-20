class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        row_dict = {}
        col_dict = {}

        while i < 9:
            j=0
            while j < 9:
                cell_set = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] is not '.':
                            if board[i+k][j+l] in cell_set or (i+k,board[i+k][j+l]) in row_dict or (j+l,board[i+k][j+l]) in col_dict:
                                return False
                            else:
                                cell_set.add(board[i+k][j+l])
                                row_dict[(i+k,board[i+k][j+l])] = 1
                                col_dict[(j+l,board[i+k][j+l])] = 1
                j+=3

            i+=3
        
        return True

            