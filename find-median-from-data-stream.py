class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap, num)
        elif num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap,-1*num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            top = -1*heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, top)
        elif len(self.min_heap) - len(self.max_heap) > 1:
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1*top)

    def findMedian(self) -> float:
      
        if len(self.min_heap) == len(self.max_heap):
            res = (self.min_heap[0] + -1*self.max_heap[0])/2
        elif len(self.min_heap) > len(self.max_heap):
            res = self.min_heap[0]
        else:
            res = -1*self.max_heap[0]
        # print(self.min_heap,self.max_heap)
        return res



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()