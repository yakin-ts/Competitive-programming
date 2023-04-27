class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        locked = set()
        for i in range(1,N):
            locked.add(i)
        que  = deque([0])
        visited = set([0])
        while que:
            n = que.popleft()
            unlock = rooms[n]
            for x in unlock:
                if x not in visited:
                    visited.add(x)
                    que.append(x)
                    locked.remove(x)
        return len(locked)==0