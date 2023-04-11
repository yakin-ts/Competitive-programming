"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = defaultdict()
        for emp in employees:
            graph[emp.id] = {'importance':emp.importance,'subordinates':emp.subordinates}
            
        visited = set()
        total_imp = 0

        def dfs(node):
            nonlocal total_imp
            if not node:
                return
            if node not in visited:
                visited.add(node)
            total_imp += graph[node]['importance']
            for nd in graph[node]['subordinates']:
                dfs(nd)
           
            return total_imp

        return dfs(id)