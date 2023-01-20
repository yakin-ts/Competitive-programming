class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        top = False
        idx = 0
        last = len(arr)-1
        if len(arr)<=2:
            return False
        else:
             while idx < len(arr)-1:
                    if arr[idx]==arr[idx+1] :
                        return False
                    else:
                        if top==False:
                            if arr[idx] > arr[idx+1]:
                                if idx==0:
                                    return False
                                elif idx+1==last:
                                    return True
                                top = True
                            else:
                                if idx+1==last:
                                    return False
                        elif top==True:
                            if arr[idx] < arr[idx+1]:
                                return False
                    idx +=1
        return True
                