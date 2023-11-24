class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        changes = defaultdict(list)
        for w in wordList:
            for i in range(L):
                changes[w[:i]+'*'+w[i+1:]].append(w)
        que = deque([[beginWord, 1]])
        visited = {beginWord}

        while que:
            node, step = que.popleft()
            for i in range(L):
                tmp = node[:i] + '*' + node[i+1:]
                for w in changes[tmp]:
                    if w==endWord:
                        return step + 1
                    if w not in visited:
                        que.append([w,step+1])
                        visited.add(w)
        return 0

