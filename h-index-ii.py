class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        N = len(citations)
        right = N-1

        while right >= left:
            mid = left + (right - left)//2
            dist = N - mid
            if citations[mid] == dist:
                return dist
            elif citations[mid] > dist:
                right = mid -1
            else:
                left = mid + 1
        

        return N - left