# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left_count = 0
        right_count = 0
        left = None
        right = None

        def helper(node):
            nonlocal left_count, right_count, left, right
            if not node:
                return 0
            left_count +=1
            if left_count == k:
                left = node
            helper(node.next)
            right_count += 1
            if right_count == k:
                right = node
        helper(head)
        left.val, right.val = right.val, left.val
        return dummy.next