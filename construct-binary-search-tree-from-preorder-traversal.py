# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def helper(tree,num):
            if not tree:
                node = TreeNode(num)
                return node
            elif tree.val <= num:
                tree.right = helper(tree.right, num)
            else:
                tree.left = helper(tree.left, num)
            return tree
            

        root = None
        for elem in preorder:
            if not root:
                root = TreeNode(elem)
            else:
                helper(root,elem)
        return root