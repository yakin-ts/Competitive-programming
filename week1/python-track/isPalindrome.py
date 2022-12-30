class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        str_x = str(x)
        l=0
        r=len(str_x)-1
        while r>=l:
            if r!=l and str_x[l] is not str_x[r]:
                return False
            l+=1
            r-=1
        return True
        