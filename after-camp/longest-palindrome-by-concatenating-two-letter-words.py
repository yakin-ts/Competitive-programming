class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        self.map = {}

        def pal(stx):
            if not stx:
                return ''
            return pal(stx[1:]) + stx[0]
        def isPalidrome(stx):
            left = 0
            right = len(stx) - 1
            while right > left:
                if stx[left]!=stx[right]:
                    return False
                left +=1
                right -=1
            return True
        
        count = Counter(words)
        ans = 0
        single = 0
        processed = set()
        print(count)
        for key, val in count.items():
            k2 = pal(key)
            isPali = isPalidrome(key)
            if isPali and val%2!=0:
                single = 2
                ans += 2*val - 2
            if isPali and val%2==0:
                ans += 2*val
            if key in processed or k2 in processed:
                continue
            if k2 in count and not isPali :
                ans += 4*min(count[k2],val)
                processed.add(key)
                processed.add(k2)
        return ans + single
            
            

        