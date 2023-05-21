class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.root = [i for i in range(len(s))]  
        self.rank = [0 for _ in range(len(s))]  
 
        for x, y  in pairs:
            self.union(self.root[x],self.root[y])
        stx = defaultdict(list)

        for i in range(len(s)):
            root = self.find(i)
            stx[root].append(s[i])

        for st in stx.values():
            st.sort(reverse=True)

        answer = []
        for i in range(len(s)):
            root = self.find(i)
            answer.append(stx[root].pop())
        return ''.join(answer)

    def find(self,node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self,node1, node2):
        root_x = self.find(node1)
        root_y = self.find(node2)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1