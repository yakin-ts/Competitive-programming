class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R , C = len(board), len(board[0])
        visited = [ [False for _ in range(C)] for _ in range(R)]
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1)]
        res = 0 

        def inbound(row,col):
            return (0 <=row <R) and( 0<= col<C)
        
        def adjacent(row,col):
            count = 0
            for x,y in directions:
                if inbound(row+x,col+y) and board[row+x][col+y]=='M':
                    count += 1
            return count

        def DFS(row,col):
            nonlocal res
            if inbound(row,col) and not visited[row][col]:
                visited[row][col]=True
                adj_count = adjacent(row,col)

                if adj_count==0:
                    board[row][col] ='B'
                else:
                    board[row][col]= str(adj_count)
                    return board
                
                for x,y in directions:
                    DFS(row+x,col+y)
                    
            return board

        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        return DFS(click[0],click[1])

                

