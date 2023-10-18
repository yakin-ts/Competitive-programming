# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def placeholder(num,node):
            head = ListNode()
            cur = head
            for _ in range(num-1):
                cur.next = ListNode()
                cur = cur.next
            cur.next = node
            return head


        count1 =0
        count2=0
        cur = l1
        while cur:
            count1 +=1
            cur = cur.next
        cur = l2
        while cur:
            count2 +=1
            cur = cur.next
        
        if count1 > count2:
            diff = count1 -count2
            l2 = placeholder(count1 -count2,l2)
        elif count2 > count1:
            l1 = placeholder(count2 - count1,l1)
        ans = []
        carry = [0]
        def addition(node1,node2):
            if not node1 or not node2:
                return None
            addition(node1.next,node2.next)
            print(node1.val,node2.val)
            tmp = node1.val + node2.val + carry[-1]
            if tmp > 9:
                ans.append(tmp - 10)
                carry.append(1)
            else:
                ans.append(tmp)
                carry.append(0)
        addition(l1,l2)
        res = []
        if carry[-1] >0:
            res.append(carry[-1])
        res.extend(ans[::-1])
        ll = ListNode()
        cur = ll
        for x in res:
            cur.next = ListNode(x)
            cur = cur.next
        return ll.next