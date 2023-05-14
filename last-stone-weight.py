class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        last = 0
        heap = []
        for s in stones:
            heapq.heappush(heap,-1*s)
        
        while len(heap) >=2:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if y!=x:
                heapq.heappush(heap,y-x)
        return -1*heap[-1] if heap else 0