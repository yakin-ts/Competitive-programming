class DSU:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self,x):
        if x==self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1

    def connected(self,x,y):
        return self.find(x)==self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        uf = DSU(N)

        dists = []
        for i in range(N):
            for j in range(i+1,N):
                dists.append((abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1]),i,j))
        
        dists.sort()
        cost = 0
        for dist, i, j in dists:
            if not uf.connected(i,j):
                uf.union(i,j)
                cost += dist
        return cost