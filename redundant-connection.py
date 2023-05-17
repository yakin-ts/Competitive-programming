class DisjointSet:
    def __init__(self,size):
        self.root = [i  for i in range(size+1)]
        self.rank = [1 for _ in range(size+1)]
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def connected(self,x,y):
        return self.find(x)==self.find(y)

    def union(self,x,y):
        n1 = self.find(x)
        n2 = self.find(y)
        if n1!=n2:
            if self.rank[n1] > self.rank[n2]:
                self.root[n2] = n1
            elif self.rank[n1] > self.rank[n2]:
                self.root[n1] = n2
            else:
                self.root[n2] = n1
                self.rank[n1] += 1
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = DisjointSet(len(edges))
        res = []
        for u,v in edges:
            if uf.connected(u,v):
                return [u,v]
            uf.union(u,v)