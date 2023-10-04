class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))
        heap = [(0,k)]
        distances = {i:inf for i in range(n+1)}
        distances[k] = 0
        distances[0] = 0
        visited = set()

        while heap:
            weight, node = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)

            for time, nd in graph[node]:
                dist = weight + time
                if dist < distances[nd]:
                    distances[nd] = dist
                    heapq.heappush(heap,(dist,nd))
        ans = [x for x in distances.values()]
        return max(distances.values() ) if inf not in ans else -1