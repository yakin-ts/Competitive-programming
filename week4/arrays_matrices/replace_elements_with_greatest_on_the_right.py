class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)-2
        if len(arr)==1:
            return [-1]
        for i in range(len(arr)-1):
            if i == length:
                arr[i]= max(arr[i+1:])
                arr[i+1]=-1
            else:
                arr[i] = max(arr[i+1:])
            
        return arr