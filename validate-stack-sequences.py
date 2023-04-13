class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        l=0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1]==popped[l]:
                stack.pop()
                l+=1
        return len(stack)==0