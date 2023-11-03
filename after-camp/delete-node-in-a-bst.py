# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val< key:
            root.right =  self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                inorder = self.find_min(root.right)
                root.val = inorder.val
                root.right = self.deleteNode(root.right, inorder.val)
        return root
    def find_min(self,node):
        cur=node

        while cur.left:
            cur = cur.left
        return cur