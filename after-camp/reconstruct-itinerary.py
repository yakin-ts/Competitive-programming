class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        graph = defaultdict(list)
        for u , v in tickets:
            graph[u].append(v)
        for k in graph:
            graph[k].sort(reverse=True)
        res = []
        def dfs(node):
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            res.append(node)
        dfs('JFK')
        return res[::-1]



