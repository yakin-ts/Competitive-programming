# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        fast_count = 0
        slow_count = 0
        if not head.next: return None
        while fast:
            while fast:
                fast_count += 1
                fast = fast.next
            while slow and slow_count + 1 < (fast_count//2)  :
                slow_count += 1
                slow = slow.next
            slow.next = slow.next.next if slow.next else None
        return head