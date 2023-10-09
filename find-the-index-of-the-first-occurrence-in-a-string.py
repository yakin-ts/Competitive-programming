class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(needle)
        def build_lps(stx):
            LPS = [0 for _ in range(len(stx))]
            i,j = 0,1

            while j < len(stx):
                if stx[i]==stx[j]:
                    LPS[j] = i+1
                    i+=1
                    j+=1
                else:
                    if i==0:
                        j+=1
                    else:
                        i = LPS[i-1]
            return LPS
        lps = build_lps(needle)

        p , t = 0,0

        while t < len(haystack):
            if needle[p]==haystack[t]:
                p+=1
                t+=1
            elif p==0:
                t+=1
            else:
                p = lps[p-1]
            if p==N:
                return t-p
        return -1