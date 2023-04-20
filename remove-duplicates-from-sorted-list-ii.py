class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # check for duplicates at the beginning
        while head and head.next and head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
        if not head or not head.next:
            return head
        
        prev = None
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                if prev:
                    prev.next = cur.next
                else:
                    prev = cur
            else:
                prev = cur
            cur = cur.next
        return head