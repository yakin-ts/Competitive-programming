# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []

        res = []
        def bfs(node):
            que = deque([node])
            tot = float(node.val)
            res = [tot]

            while que:
                que_len = len(que)
                count = 0
                tot = 0.0
                for _ in range(que_len):
                    node = que.popleft()
                    if node.left:
                        tot += float(node.left.val)
                        que.append(node.left)
                        count +=1
                    if node.right:
                        tot += float(node.right.val)
                        que.append(node.right)
                        count +=1
                if count > 0:
                    res.append(tot/count)
                
            return res
        return bfs(root)