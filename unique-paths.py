class Solution:
    def uniquePaths(self, m: int, n: int, mem={}) -> int:
        # if (m,n) in mem:
        #     return mem[(m,n)]
        # if m==1 and n==1:
        #     return 1
        # if m==0 or n==0:
        #     return 0
        
        # mem[(m,n)] = self.uniquePaths(m-1,n,mem) + self.uniquePaths(m,n-1,mem)

        # return mem[(m,n)]

        row_fact = factorial(m-1)
        col_fact = factorial(n-1)
        paths = factorial(n+m-2)//(row_fact*col_fact)

        return paths