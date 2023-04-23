class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Create a dummy node before the head
        dummy = ListNode(0)
        dummy.next = head
        
        # Traverse the list from the second node to the end
        curr = head
        while curr and curr.next:
            # If the next node is smaller than the current node,
            # remove the next node from the list and find its insertion point
            if curr.next.val < curr.val:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next
                # Insert the next node at its insertion point
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
            else:
                # Move to the next node
                curr = curr.next
                
        # Return the sorted list
        return dummy.next