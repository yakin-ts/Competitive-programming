# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count +=1
            temp= temp.next
        mid = ceil(count/2) if count%2==1 else count/2 +1
        while mid>1:
            head = head.next
            mid-=1
        return head