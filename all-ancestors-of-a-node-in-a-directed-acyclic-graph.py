class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        incoming = [0]*n
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            incoming[v]  += 1
        
        que = deque([])

        for i in range(n):
            if incoming[i]==0:
                que.append(i)
        
        ancestors = [ set() for _ in range(n)]

        while que:
            node = que.popleft()

            for nd in graph[node]:
                incoming[nd] -=1
                ancestors[nd].add(node)
                ancestors[nd].update(ancestors[node])

                if incoming[nd]==0:
                    que.append(nd)

        ancestors = [ (sorted(list(st))) for st in ancestors]

                

        return ancestors