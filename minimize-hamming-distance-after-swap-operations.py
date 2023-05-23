class UnionFind:
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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        uf = UnionFind(len(source))

        for i, j in allowedSwaps:
            uf.union(i,j)
    
        connection = defaultdict(list)
        for i in range(len(source)):
            connection[uf.find(i)].append(i)
        
        result = 0
        for _ , group in connection.items():
            count = defaultdict(int)
            for i in group:
                count[source[i]] += 1
                count[target[i]] -= 1
                
            for c in count.values():
                if c>0:
                    result += c


        return result