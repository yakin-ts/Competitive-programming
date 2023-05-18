class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        

        root = defaultdict(str)
        def initialize_ds(stx1,stx2):
            for c in stx1:
                root[c] = c
            for c in stx2:
                root[c] = c
        initialize_ds(s1,s2)

        def find(x):
            if x == root[x]:
                return root[x]
            root[x] = find(root[x])
            return root[x]
            
        def union(x,y):
            node1 = find(x)
            node2 = find(y)
            if node1 != node2:
                if node1 < node2:
                    root[node2] = node1
                else:
                    root[node1] = node2
                    
        answer = ''

        for i in range(len(s1)):
            union(s1[i],s2[i])
        for c in baseStr:
            if c in root:
                answer += find(c)
            else:
                answer += c
        print(root)
        return answer