class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,d in flights:
            graph[u].append((d,v))
        heap = [(0,src,0)]
        distance = [float('inf')] * n  
        distance[src] = 0
        visited = {}

        while heap:
            d, v, stops =  heapq.heappop(heap)
            visited[v] = stops
            if v==dst:
                return d
            if stops > k:
                continue
            for w, node in graph[v]:
                dist = d + w
                if node in visited and visited[node] <= stops:
                    continue
                heapq.heappush(heap,(dist,node,stops+1))
        
        return -1