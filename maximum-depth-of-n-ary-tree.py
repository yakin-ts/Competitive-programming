"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        visited = set()

        def dfs(node,count):
            nonlocal max_depth
            if not node:
                return
            # visited.add(node.val)
            count += 1
            max_depth = max(max_depth,count)
            for nd in node.children:
                dfs(nd,count)
        dfs(root,0)
        return max_depth