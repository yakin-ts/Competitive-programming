class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = {} 
        def find(x):
            if x not in root:
                root[x] = x
            elif root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root[find(x)] = find(y)

        for x, y in stones:
            union(x, y)
        reps = {find(x) for x in root}

        return len(stones) - len(reps)