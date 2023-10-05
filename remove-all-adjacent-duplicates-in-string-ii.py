class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        last = ''
        for ch in s:
            if not stack or stack[-1][0]!=ch:
                stack.append((ch,1))
            else:
                if stack[-1][1]+1==k:
                    while stack and stack[-1][0]==ch:
                        stack.pop()
                else:
                    stack.append((ch,stack[-1][1]+1))
            
        return "".join([ch for ch,_ in stack])