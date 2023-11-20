class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_mem = {}
        t_mem = {}

        for i in range(len(s)):
            if s[i]  in s_mem and s_mem[s[i]] != t[i]:
                return False
            if t[i]  in t_mem and t_mem[t[i]] != s[i]:
                return False
            s_mem[s[i]] = t[i]
            t_mem[t[i]] = s[i]
            
        return True
            

        