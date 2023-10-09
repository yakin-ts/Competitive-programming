# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(node,row,col,d):
            if not node:
                return 
            else:
                if row in d:
                    d[row]['mn'] = min(d[row]['mn'],col)
                    d[row]['mx'] = max(d[row]['mx'],col)
                else:
                    d[row] = dict()
                    d[row]['mn'] = col
                    d[row]['mx'] = col
            left = helper(node.left,row + 1,2*col,d)
            right = helper(node.right,row+1,2*col + 1,d)
        
        res = {}
        helper(root,0,0,res)
        max_width = -inf

        for w in res.keys():
            max_width = max(max_width, 1 + res[w]['mx'] - res[w]['mn'])
        return max_width


            
        return helper(root,0)