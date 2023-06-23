class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        idx = len(arr) - 2
        while idx >=0 and arr[idx] <= arr[idx+1]:
            idx -=1
        if idx==-1:
            return arr
        idx2 = len(arr)-1
        while arr[idx2] >= arr[idx] or arr[idx2]==arr[idx2-1]:
            idx2 -=1
        arr[idx], arr[idx2] = arr[idx2], arr[idx]

        return arr