class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        answer = 0
        N = len(costs)//2
        A,B = 0,0
        new_costs = sorted(costs, key=lambda arr:abs(arr[0]-arr[1]),reverse=True)

        for cost in new_costs:
            if (B < N and cost[0] >= cost[1]) or A==N:
                answer += cost[1]
                B +=1
            else:
                answer += cost[0]
                A += 1
        return answer