class Solution:
    def average(self, salary: List[int]) -> float:
       mnm = min(salary)
       mxm = max(salary)
       return (sum(salary)-(mnm + mxm))/(len(salary)-2)

