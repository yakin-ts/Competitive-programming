# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head

        count = 0
        cur = head
        mem = defaultdict()
        def rotate(node):
            nonlocal cur, count
            if not node:
                return
            rotate(node.next)
            count += 1
            mem[count] = node
        
        rotate(head)

        if k > count:k %= count
        if count==1 or count==k or k==0: return head

        new_head = mem[k]
        mem[k+1].next = None
        while new_head and new_head.next:
            new_head = new_head.next
        new_head.next = head
        head = mem[k]


        return head