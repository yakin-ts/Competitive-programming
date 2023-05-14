class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        end_pos = defaultdict(list)

        for num in nums:
            if  end_pos[num - 1]:
                end = heapq.heappop(end_pos[num - 1])
                heapq.heappush(end_pos[num], end + 1)
            else:
                heapq.heappush(end_pos[num], 1)
        print(end_pos)
        for key , val in end_pos.items():
            if val and min(val) < 3:
                return False

        return True