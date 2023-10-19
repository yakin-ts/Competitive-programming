class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref = [None] * n
        for i in range(n):
            pref[i] = {}
            for j in range(n - 1):
                pref[i][preferences[i][j]] = j

        friends = [None] * n
        for u, v in pairs:
            friends[u] = v
            friends[v] = u

        count = 0

        for x in range(n):
            for u in range(n):
                if u != x:
                    v = friends[x]
                    y = friends[u]
                    if (pref[x][u] < pref[x][v] and pref[u][x] < pref[u][y]):
                        count += 1
                        break

        return count