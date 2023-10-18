# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = self.helper(root,[])
        ans.sort()
        return ans[k-1]

    def helper(self,node,arr):
        if not node:
            return
        arr.append(node.val)
        self.helper(node.left,arr)
        self.helper(node.right,arr)

        return arr