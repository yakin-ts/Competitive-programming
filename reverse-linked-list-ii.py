# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head

        l_ptr = None
        count = 1
        cur = head
        while cur:
            if count==left:
                l_ptr = cur
            elif count > left:
                if count <= right:
                    ct = left
                    nd = l_ptr
                    while ct  <= count:
                        tmp = nd.val
                        nd.val = cur.val
                        cur.val = tmp
                        ct +=1
                        nd = nd.next
            count += 1
            cur = cur.next
        return head