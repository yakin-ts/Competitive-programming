# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = defaultdict(int)
        idx = 0
        while head:
            if head not in visited:
                visited[head] = idx
                head = head.next
            else:
                return head

        return None