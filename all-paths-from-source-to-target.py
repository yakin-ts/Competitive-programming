class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def dfs(node,arr):
            nonlocal paths
            arr.append(node)
            if node == len(graph)-1:
                paths.append(arr.copy())
            for x in graph[node]:
                dfs(x,arr)
                arr.pop()
            return paths
            
        return dfs(0,[])