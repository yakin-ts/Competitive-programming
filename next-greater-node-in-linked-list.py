# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        values = []
        result = []
        idx= 0
        
        while head:
            values.append(head.val)
            result.append(0)
            while stack and values[stack[-1]] < head.val:
                result[stack.pop()] = head.val
            stack.append(idx)
            idx += 1
            head = head.next
        
        return result