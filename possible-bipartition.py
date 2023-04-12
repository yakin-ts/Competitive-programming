class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dis in dislikes:
            graph[dis[0]].append(dis[1])
            graph[dis[1]].append(dis[0])
        
        visited = [-1 for _ in range(n+1)]

        def dfs(node,color):
            if visited[node]!=-1:
                return color==visited[node]
            visited[node] = 1 if color==1 else 0
            for nd in graph[node]:
                vis = dfs(nd,1-color)
                if not vis:
                    return False
            return True
        
        for i in range(1,n+1):
            if visited[i]==-1:
                ans = dfs(i,0)
                if not ans: return False
        return True