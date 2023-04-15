# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        root_leaf= 0
        def dfs(node,num):
            nonlocal root_leaf
            # nonlocal paths
            num += str(node.val)
            if not node.left and not node.right:
                root_leaf += int(num) if num else 0
                return root_leaf
            if node.left:
                dfs(node.left,num)
            if node.right:
                dfs(node.right,num)

            return root_leaf

        return dfs(root,'')