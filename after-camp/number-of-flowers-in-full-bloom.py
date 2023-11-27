class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        regions = {}

        for f in flowers:
            regions[f[0]] = regions.get(f[0], 0) + 1  
            regions[f[1] + 1] = regions.get(f[1] + 1, 0) - 1  

        regions = dict(sorted(regions.items(), key=lambda v: v[0]))
        acc_val = list(accumulate(regions.values()))

        keys = list(regions.keys())
        graph = {}  
        for k, v in zip(keys, acc_val):
            graph[k] = v

        ans = []
        for p in people:
            if p < keys[0] or p > keys[-1]:
                ans.append(0)
                continue

            x_axis = bisect.bisect_right(keys, p) - 1
            ans.append(graph[keys[x_axis]])

        return ans
