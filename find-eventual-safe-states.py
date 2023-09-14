class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        revGraph = defaultdict(list)
        incoming = [0]*N

        for i in range(N):
            for nd in graph[i]:
                revGraph[nd].append(i)
                incoming[i] +=1
        print(revGraph)
        que = deque([])

        for i in range(N):
            if incoming[i] == 0:
                que.append(i)

        order = []
        safe = [False]*N
        while que:
            node = que.popleft()
            safe[node] = True

            for x in revGraph[node]:
                incoming[x] -=1

                if incoming[x]==0:
                    que.append(x)
        for i in range(N):
            if safe[i]:
                order.append(i)
        return order