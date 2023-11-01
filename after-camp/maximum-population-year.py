class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        early , maxPeople = 1950, 0

        for yr in range(1950, 2051):
            count = 0
            for start, end in logs:
                if start <= yr < end:
                    count+=1
            if count > maxPeople:
                maxPeople = count
                early = yr
        return early
        



        