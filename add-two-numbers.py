# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        head = dummy

        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            add = num1 + num2 + carry
            head.next = ListNode(add%10)
            head = head.next
            carry = add//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            head.next = ListNode(carry)
        
        return dummy.next