class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for i, edge in enumerate(equations):
            graph[edge[0]].append((edge[1],values[i]))
            graph[edge[1]].append((edge[0],1/values[i]))

        def dfs(node,target,product):
            if node not in graph or target not in graph:
                return -1.0
            if node not in visited:
                visited.add(node)
                if node==target:
                    return product
                
                for nbr, val in graph[node]:
                    result = dfs(nbr,target,product*val)
                    if result != -1.0:
                        return result
            return -1.0

        answer = []

        for a,b in queries:
            visited = set()
            answer.append(dfs(a,b,1))
        return answer
                
                
            


        