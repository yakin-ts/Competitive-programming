class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        graph = defaultdict(list)
        ans =0

        def inbound(x1,y1,r1,x2,y2,r2):
            return r1**2 >= (x1-x2)**2 + (y1-y2)**2 
              
        for i in range(N):
            X, Y ,R = bombs[i]
            for j in range(i+1,N):
                x,y, r  = bombs[j]
                if inbound(X,Y,R,x,y,r):
                    graph[i].append(j)
                if inbound(x,y,r,X,Y,R):
                    graph[j].append(i)
        
        
        def dfs(node,visited):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei,visited)
            
        
        for i in range(N):
            vis = set([i])
            dfs(i,vis)
            ans = max(ans,len(vis))

        return ans