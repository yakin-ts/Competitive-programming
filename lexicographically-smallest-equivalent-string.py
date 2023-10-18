class UnionFind:
    def __init__(self,stx1,stx2):
        self.root={}
        for ch in stx1:
            self.root[ch] = ch
        for ch in stx2:
            self.root[ch] = ch
    def find(self,stx):
        if stx==self.root[stx]:
            return self.root[stx]
        self.root[stx] = self.find(self.root[stx])
        return self.root[stx]
    
    def union(self,ch1,ch2):
        x = self.find(ch1)
        y = self.find(ch2)
        if x!=y:
            if x > y:
                self.root[x] = y
            else:
                self.root[y] = x
        
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        N = len(s1)
        uf = UnionFind(s1,s2)
        for i in range(N):
            uf.union(s1[i],s2[i])
        
        answer = ''
        for ch in baseStr:
            if ch in uf.root:
                answer += uf.find(ch)
            else:
                answer += ch
        return answer