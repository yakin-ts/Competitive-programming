class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [n for n in nums]
        for i,n in enumerate(self.arr):
            if i>0:
                self.arr[i] += self.arr[i-1]

        

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right] - self.arr[left-1] if left > 0 else self.arr[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)