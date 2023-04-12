class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [-1 for _ in range(len(graph))]

        def dfs(node,color):
            if visited[node]!=-1:
                return color==visited[node]
            visited[node] = color

            for nd in graph[node]:
                temp = dfs(nd,1-color)
                if not temp:
                    return False
            return True

        ans = True
        for i in range(len(graph)):
            if visited[i]==-1:
                ans &= dfs(i,0)
        return ans