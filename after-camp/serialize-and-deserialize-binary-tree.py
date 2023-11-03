# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        stx = []
        def helper(node):
            if not node:
                stx.append("*")
                return 
            stx.append(str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)

        return ",".join(stx)


    def deserialize(self, data):
        idx = 0
        N = len(data)
        def dfs():
            nonlocal idx
            if idx>=N:
                return None
            if data[idx]=='*':
                idx+=1
                return None
            tree = TreeNode(int(data[idx]))
            idx+=1
            tree.left = dfs()
            tree.right=dfs()

            return tree
        data = data.split(",")
        return dfs()
            
            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))