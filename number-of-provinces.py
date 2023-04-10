# class UnionFind:
#     def __init__(self,size):
#         self.root = [i for i in range(size)]
#         self.rank = [1 for _ in range(size)]
#         self.count = size
#     def find(self,x):
#         if x==self.root[x]:
#             return x
#         self.root[x] = self.find(self.root[x])
#         return self.root[x]
    
#     def union(self,x,y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             self.count -=1
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.root[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.root[rootX] = rootY
#             else:
#                 self.root[rootY] = rootX
#                 self.rank[rootX] +=1
#     def connected(self,x,y):
#         return self.find(x)==self.find(y)
#     def totalProvinces(self):
#         return self.count

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # N = len(isConnected)
        # uf = UnionFind(N)
        # for i,con in enumerate(isConnected):
        #     for j,node in enumerate(con):
        #         if i!=j and node==1:
        #             uf.union(i,j)
        # return uf.totalProvinces()

        # Approach 2

        graph = defaultdict(list)

        for i,con in enumerate(isConnected):
            for j, x  in enumerate(con):
                if x==1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = set()

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for x in graph[node]:
                    dfs(x)
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                count +=1
                dfs(i)
        return count