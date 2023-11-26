class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacency_list = defaultdict(set)
        for i, n in enumerate(manager):
            if n != -1:
                adjacency_list[n].add(i)
    
        q = deque()
        answer = informTime[headID]
        q.append((headID, 0))
        res = answer
        while q:
            manager, tempInformTime = q.popleft()
            res = max(res, tempInformTime)
            for nd in adjacency_list[manager]:
                q.append((nd, informTime[manager] + tempInformTime))
            
        return res

    