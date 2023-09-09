class Solution:
    def countSubTrees(self,n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        result = [0] * n
        visited = [False] * n
        
        def dfs(node):
            visited[node] = True
            freq = defaultdict(int)
            freq[labels[node]] += 1
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    sub_freq = dfs(neighbor)
                    for label, count in sub_freq.items():
                        freq[label] += count
            
            result[node] = freq[labels[node]]
            return freq
        
        dfs(0)
        return result