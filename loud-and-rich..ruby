class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        #Let len(richer) = n and let len(quiet) = m!
        #Time: O(n + m + m + m*m + m +  m) -> O(m^2 + n)
        #Space: O(m*m + m + m + m*m + m) -> O(m^2)
        #step 1: build adjacency list representation and update indegrees of every node initially!
        adj = [[] for _ in range(len(quiet))]
        indegrees = [0] * len(quiet)
        #we want edges to go from richer to poorer so that ancestors of every node are all people
        #who have more money than the node person!
        for rel in richer:
            richer, poorer = rel[0], rel[1]
            adj[richer].append(poorer)
            indegrees[poorer] += 1
        
        queue = deque()
        ancestors = []
        for i in range(len(quiet)):
            new = set()
            new.add(i)
            ancestors.append(new)
        #step 2: fill in the queue all nodes that have indegrees of 0!

        #step 3: proceeding with Kahn's algorithm and recording list of all ancestors to every node!
        while queue:
            cur = queue.pop()
            for neighbor in adj[cur]:
                ancestors[neighbor].add(cur)
                ancestors[neighbor].update(ancestors[cur])
                indegrees[neighbor] -= 1
                if(indegrees[neighbor] == 0):
                    queue.append(neighbor)
        
        ancestors = [list(s) for s in ancestors]
        output = []
        #step 4:for each person, find the least quiet person who also has more money than the current               #person we're iterating on!
        for a in range(len(ancestors)):
            cur_ancestors = ancestors[a]
            if(len(cur_ancestors) == 1):
                output.append(a)
                continue
            minimum = cur_ancestors[0]
            for ancestor in cur_ancestors:
                #check if current person with more money than person a has lower quiet level!
                if(quiet[ancestor] < quiet[minimum]):
                    minimum = ancestor
            output.append(minimum)
        return output