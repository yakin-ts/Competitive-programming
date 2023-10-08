class Solution:
    def knightDialer(self, n: int) -> int:

        def inbound(r,c):
            if r==3 and (c==0 or c==2):
                return False
            return 0<=r<4 and 0<=c<3
        directions = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]
        mem = {}
        def dp(r,c,num):
            if num==1:
                return 1
            if (r,c,num) in mem:
                return mem[(r,c,num)]
            result = 0
            for x, y in directions:
                if inbound(r+x,c+y):
                    result +=dp(r+x,c+y,num-1)
            mem[(r,c,num)] = result
            return result
        
        ans = 0
        for i in range(4):
            for j in range(3):
                if inbound(i,j):
                    ans  += dp(i,j,n) 
            
        return ans%(10**9+7)