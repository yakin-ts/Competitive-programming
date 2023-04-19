# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur  = head
        odd,even,oddStart,evenStart = None,None,None,None
        count = 1 
        while cur:
            if count%2==0:
                if not even:
                    even = cur
                    evenStart = cur
                else:
                    even.next = cur
                    even = even.next
                    
            else:
                if not odd:
                    odd = cur
                    oddStart = cur
                else:
                    odd.next = cur
                    odd = odd.next
                    
            cur = cur.next
            count +=1
        if even:
            even.next = None
        if odd:
            odd.next = evenStart
        return oddStart