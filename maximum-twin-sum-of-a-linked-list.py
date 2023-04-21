# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mem = defaultdict()
        rev_idx = 0
        max_twin = 0
        idx = 1

        def recursive(node):
            nonlocal  idx,rev_idx, max_twin
            if not node:
                return 
            mem[idx] = node.val
            idx +=1
            recursive(node.next)
            rev_idx += 1
            max_twin = max(max_twin,mem[rev_idx] + node.val)

            return max_twin
        return recursive(head)