class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        normal = 0
        time = 0
        R = len(grid)
        C = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    normal +=1
                elif grid[i][j]==2:
                    queue.append((i,j))
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def inbound(row,col):
            return 0<=row<R and 0<=col<C

        while queue:
            que_len = len(queue)
            for _ in range(que_len):
                r,c = queue.popleft()
                found = False
                for x,y in directions:
                    if inbound(r+x,c+y) and grid[r+x][c+y]==1:
                        queue.append((r+x,c+y))
                        grid[r+x][c+y] = 2
                        normal -=1           
            if queue:
                time +=1
        return time if normal==0 else -1