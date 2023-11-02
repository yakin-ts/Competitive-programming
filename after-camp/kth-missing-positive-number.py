class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur = 1
        count,idx = 0,0
        N = len(arr)
        while count < k:
            if idx < N:
                if arr[idx]!=cur:
                    count+=1
                    if count==k:
                        return cur
                else:
                    idx +=1
                cur+=1
                    
            else:
                return arr[-1] + k - count
