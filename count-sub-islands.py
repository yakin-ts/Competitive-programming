class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        def inbound(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(row,col):
            if not inbound(row,col) or visited[row][col] or grid2[row][col]==0 :
                return True
            
            visited[row][col] = True
            flag = True
            if grid1[row][col]==0:
                flag = False

            for x, y in directions:
                flag  = dfs(row+x,col+y) and flag
                
            return flag

        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid2[i][j]==1 and dfs(i,j):
                    count +=1
                    

        return count