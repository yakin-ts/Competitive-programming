class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = [[(-1,0)] for _ in range(10**5)]
        self.snap_count = 0
        
    def set(self, index: int, val: int) -> None:
        self.snapshot[index].append((self.snap_count,val))
        

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1
  

    def get(self, index: int, snap_id: int) -> int:
        arr = self.snapshot[index]

        N = len(arr)
        
        left = 0
        right = N - 1
        idx = float('-inf')
        while right >= left :
            mid = left + (right - left)//2
            if arr[mid][0] > snap_id:
                right = mid - 1
            else:
                idx = mid
                left = mid + 1
        return arr[idx][1] if idx >= 0 else 0
        
            


        return self.snapshot[index][snap_id]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)