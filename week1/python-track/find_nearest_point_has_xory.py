class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = math.inf
        idx = -1

        for i, point in enumerate(points):
            if point[0]==x or point[1]==y:
                tmp = abs(x-point[0]) + abs(y-point[1])
                if min_distance==math.inf or tmp < min_distance:
                    min_distance = tmp
                    idx = i
        return idx