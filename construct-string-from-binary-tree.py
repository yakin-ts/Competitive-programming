# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        path = ''
        def dfs(node):
            nonlocal path
            if not node:
                return
            path +=( str(node.val)+'(')
            dfs(node.left)
            path += ')('
            dfs(node.right)

            if path[-1:]=='(':
                path = path[:-1]
            else:
                path += ')'
            if path[-2:]=='()':
                path = path[:-2]
            return path
        
        return dfs(root)
         