class Solution:
    def soupServings(self, n: int) -> float:
        mem = {}
        def solve(a,b):
            if (a,b) in mem:
                return mem[(a,b)]
            if a<=0 and b<=0:
                return 0.5
            if a<=0:
                return 1
            if b<=0:
                return 0
            mem[a,b] = 0.25*solve(a-100,b) + 0.25*solve(a-75,b-25) + 0.25*solve(a-50,b-50) + 0.25*solve(a-25,b-75)
            return mem[(a,b)]
        
        return solve(n,n) if n < 10000 else 1
            