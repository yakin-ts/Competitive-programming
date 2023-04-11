class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        LAND = 1
        WATER = 0
        self.max_area = 0
        visited = [[False for _  in  range(C)] for _ in range(R)]

        def inbound(row,col):
            return 0<=row<R and 0<=col<C

        max_area = 0
        def dfs(row,col):
            nonlocal max_area
            if inbound(row,col) and not visited[row][col]:
                visited[row][col] = True
                if grid[row][col] == 1:
                    max_area += 1
                    dfs(row-1,col)
                    dfs(row,col-1)
                    dfs(row,col+1)
                    dfs(row+1,col)
            return max_area
        
        answer = 0
        for i in range(R):
            for j in range(C):
                if not visited[i][j]:
                    max_area = 0
                    dfs(i,j)
                    answer = max(answer,max_area)
        return answer