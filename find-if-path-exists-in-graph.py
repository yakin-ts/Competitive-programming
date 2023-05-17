class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            found = False
        def dfs(src,visited):
            nonlocal found
            if src==destination:
                return True
            visited.add(src)
            for node in graph[src]:
                if node not in visited:
                    found = dfs(node,visited)
                if found:
                    return True
        vstd = set()
        return dfs(source,vstd)