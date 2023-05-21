from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.root = {}  
        self.rank = {}  
        self.name = {}  

        def find(node):
            if self.root[node] != node:
                self.root[node] = find(self.root[node])
            return self.root[node]

        def union(node1, node2):
            root_x = find(node1)
            root_y = find(node2)
            if root_x != root_y:
                if self.rank[root_x] < self.rank[root_y]:
                    self.root[root_x] = root_y
                elif self.rank[root_x] > self.rank[root_y]:
                    self.root[root_y] = root_x
                else:
                    self.root[root_y] = root_x
                    self.rank[root_x] += 1

        for acc in accounts:
            name = acc[0]
            for i in range(1, len(acc)):
                email = acc[i]
                if email not in self.root:
                    self.root[email] = email
                    self.rank[email] = 0
                    self.name[email] = name
                union(acc[1], email)

        group = defaultdict(list)
        for email in self.root.keys():
            root = find(email)
            group[root].append(email)

        res = []
        for root, emails in group.items():
            name = self.name[root]
            res.append([name] + sorted(emails))

        return res