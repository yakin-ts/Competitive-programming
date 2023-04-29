class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = deque([])
        R = len(mat)
        C = len(mat[0])
        ans = [[inf for _ in range(len(mat[0]))] for _ in range(len(mat))]
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    que.append((i,j))
                    visited.add((i,j))
        def inbound(row,col):
            return 0<=row<R and 0<=col<C

        while que:

            r,c = que.popleft()

            for x,y in directions:
                if inbound(r+x,c+y) and (r+x,c+y) not in visited:
                    que.append((r+x,c+y))
                    visited.add((r+x,c+y))
                    if inbound(r,c):
                        mat[r+x][c+y] = mat[r][c] + 1
        return mat