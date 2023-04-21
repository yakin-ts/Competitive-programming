# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = head

        while cur:
            while cur and cur.val==prev.val:
                cur = cur.next
            prev.next = cur
            prev = cur
            
        return head