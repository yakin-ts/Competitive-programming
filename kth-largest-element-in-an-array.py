class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap,-1*n)
        
        for _ in range(k):
            ans = heapq.heappop(heap)
        return -1*ans