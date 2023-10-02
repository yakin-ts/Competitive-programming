class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)

        @cache
        def solve(i,j):
            if i >= N or j<0:
                return 0
            if s[i] == s[j]:
                return 1 + solve(i+1,j-1)
            return max(solve(i+1,j), solve(i,j-1))
        
        return solve(0,N-1)