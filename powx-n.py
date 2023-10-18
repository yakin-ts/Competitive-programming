class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = abs(n)
            x = 1/x
        
        def helper(base,p):
            if p==0:
                return 1
            if base==0:
                return 0
            else:
                ans = helper(base,p//2)
                if p%2==1:
                    ans = base*ans*ans
                else:
                    ans*= ans
            return ans
        return helper(x,n)