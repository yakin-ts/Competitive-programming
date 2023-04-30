class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mem = {root: None}
        cur = root
        start = None
        def traverse(node):
            nonlocal start
            if node == target:
                start = node
            if node.left:
                mem[node.left] = node
                traverse(node.left)
            if node.right:
                mem[node.right] = node
                traverse(node.right)
        traverse(cur)

        que = deque([start])
        distances = {start: 0}
        dist = 0
        while que and dist <= k:
            dist += 1
            que_len = len(que)
            for _ in range(que_len):
                node = que.popleft()
                if node.left and node.left not in distances:
                    que.append(node.left)
                    distances[node.left] = distances[node] + 1
                if node.right and node.right not in distances:
                    que.append(node.right)
                    distances[node.right] = distances[node] + 1
                parent = mem[node]
                if parent and parent not in distances:
                    que.append(parent)
                    distances[parent] = distances[node] + 1

        res = []
        for node, dist in distances.items():
            if dist == k:
                res.append(node.val)

        return res