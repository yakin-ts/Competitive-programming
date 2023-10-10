class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            u, v = edge
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        distance = [0] * n
        distance[start_node] = 0
        
        def dijkstra(graph, start):
            visited = set()
            heap = [(-1, start)]
            heap_dict = {start: 1}
            while heap:
                d, u = heappop(heap)
                if u in visited:
                    continue
                visited.add(u)
                for v, w in graph[u]:
                    new_dist = -d * w
                    if v not in heap_dict or heap_dict[v] < new_dist:
                        heap_dict[v] = new_dist
                        heappush(heap, (-1*new_dist, v))
            for i in range(n):
                if i not in heap_dict:
                    heap_dict[i] = 0
            return heap_dict
        
        dist = dijkstra(graph, start_node)
        return dist[end_node]