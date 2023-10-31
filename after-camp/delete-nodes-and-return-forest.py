# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        toDelete = set(to_delete)
        def dfs(node):
            if not node:
                return
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in toDelete:
                if not node.left and not node.right:
                    return 
                else:
                    if node.left:
                        ans.append(node.left)
                    if node.right:
                        ans.append(node.right)
                    return
            return node
        R = dfs(root)
        if R:
            ans.append(R)
        return ans

                


        