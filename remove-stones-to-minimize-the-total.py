class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for p in piles:
            heapq.heappush(heap,-1*p)
        ans = []
        
        for _ in range(k):
            num = -1*heapq.heappop(heap)
            heapq.heappush(heap,-1*(num - (num//2)))
        return -1*sum(heap)