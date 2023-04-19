# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        found = False
        count = 0
        if not head.next:
            return 
        def helper(node):
            nonlocal count
            nonlocal found
            if not node:
                return
            helper(node.next)
            count  += 1
            if count == n:
                if node and node.next:
                    node.val = node.next.val
                    node.next = node.next.next
                    found = True
            if count == n+1 and not found:
                node.next = node.next.next

            return node
        return helper(head)