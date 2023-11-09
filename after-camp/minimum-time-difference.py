class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        for pt in timePoints:
            minutes.append(int(pt[:2])*60 + int(pt[3:]))
        minutes.sort()

        ans = float('inf')

        N = len(minutes)
        for i in range(1,N):
            ans = min(ans,minutes[i]-minutes[i-1])
        ans = min(ans,60*24 - minutes[-1] + minutes[0])
        return ans

        