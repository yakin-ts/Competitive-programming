class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(list)

        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        
        max_rank = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if j in graph[i] and i in graph[j]:
                    rank = len(graph[i]) + len(graph[j]) - 1
                else:
                    rank =  len(graph[i]) + len(graph[j])
                max_rank = max(max_rank,rank)

        return max_rank
