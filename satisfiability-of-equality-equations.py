class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        def find(x):
            if x not in root:
                return ''
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
                    
        root = dict()

        for c in equations:
                x = c[0]
                y = c[-1]
                if c[1:-1]=='==':
                    if x not in root:
                        root[x] = x
                    if y not in root:
                        root[y] = y
                    union(x,y)
                   
        
        for c in equations:
                x = c[0]
                y = c[-1]
                if c[1:-1] =='!=':
                    f_x = find(x)
                    f_y = find(y)
                    if ((f_x and f_y) and f_x==f_y) or x==y:
                        return False
                   
        return True