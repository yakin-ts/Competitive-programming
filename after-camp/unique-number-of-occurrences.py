class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        freq = Counter(counter.values())

        for key, val in freq.items():
            if  val > 1:
                return False
        return True
        