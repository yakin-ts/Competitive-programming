class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        directions = [(-1,0),(0,-1),(0,1),(1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        que = deque([(0,0)]) if grid[0][0]==0 else deque([])
        count = 1
        
        def inbound(row, col):
            return 0 <= row < R and 0 <= col < C
        
        while que:
            que_len = len(que)
            for _ in range(que_len):
                r, c = que.popleft()
                if r == R-1 and c == C-1:
                    return count
                for x, y in directions:
                    if inbound(r+x, c+y) and grid[r+x][c+y] == 0:
                        grid[r+x][c+y] = 1
                        que.append((r+x, c+y))
            count +=1
        return -1