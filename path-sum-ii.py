# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []
        def dfs(node,arr):
            if not node:
                return None
            if (not node.left and not node.right) and  (arr and sum(arr)==targetSum):
                ans.append(arr)
            if node.left:
                node.left = dfs(node.left,arr+[node.left.val])
            if node.right:
                node.right = dfs(node.right,arr+[node.right.val])
        if root:
            dfs(root,[root.val])

        return ans