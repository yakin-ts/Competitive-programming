class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        R = len(grid)
        C = len(grid[0])
        self.perimeter = 0
        self.ones = 0
        
        def inbound(row,col):
            return (0 <= row < R and 0 <= col < C)
        
        def sub_perimeter(row,col):
            count = 0
            if inbound(row-1,col) and grid[row-1][col]==1:
                count -=2
            if inbound(row,col-1) and grid[row][col-1]==1:
                count-=2
            return 4 + count

        for i in range(C):
            for j in range(R):
                if grid[j][i]==1:
                    self.perimeter += sub_perimeter(j,i)
        return self.perimeter
                
        


