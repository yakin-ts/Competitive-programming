class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for  u , v in prerequisites:
            graph[v].append(u)
            incoming[u] += 1
            if v not in incoming:
                incoming[v] = 0
        que = deque([])

        for key, val in incoming.items():
            if val==0:
                que.append(key)
        if not prerequisites:
            return True
        count = 0
        visited = set()
        while que:
            count+=1
            node = que.popleft()
            visited.add(node)
            for x in graph[node]:
                incoming[x] -= 1
                if incoming[x]==0 and x not in visited:
                    que.append(x)
        return True if count==len(incoming) else False