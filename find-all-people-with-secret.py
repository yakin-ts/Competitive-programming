class UnionFind:
    def __init__(self,size):
        self.root = {}
        self.rank = {}
    def find(self,node):
        if node==self.root[node]:
            return self.root[node]
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    def union(self,node1,node2):
        if node1 not in self.root:
            self.root[node1] = node1
            self.rank[node1] = 0
        if node2 not in self.root:
            self.root[node2]  = node2
            self.rank[node2] = 0
        x = self.find(node1)
        y = self.find(node2)
        if x!=y:
            if self.rank[x] > self.rank[y]:
                self.root[y] = x
            elif self.rank[y] > self.rank[x]:
                self.root[x] = y
            else:
                self.root[x] = y
                self.rank[y] +=1



class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        time_map = defaultdict(list)
        for x,y,t in meetings:
            time_map[t].append([x,y])
        time_map = sorted(time_map.items())
        ans = {0,firstPerson}


        for time, mtng in time_map:
            dsu = UnionFind(n+1)
            for x,y in mtng:
                dsu.union(x,y)

            people = defaultdict(set)
            for i in dsu.root:
                root = dsu.find(i)
                people[root].add(i)
            
            for key, ppl in people.items():
                if ppl.intersection(ans):
                    ans.update(ppl)
        return list(ans)