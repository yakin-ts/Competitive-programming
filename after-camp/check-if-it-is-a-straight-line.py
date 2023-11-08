class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xi = coordinates[0][0]
        yi = coordinates[0][1]
        deno = coordinates[1][0] - xi
        num = coordinates[1][1] - yi
        slope = num/deno if deno!=0 else None

        for i in range(2,len(coordinates)):
            deno = coordinates[i][0] - xi
            num =coordinates[i][1] - yi
            m = num/deno if deno!=0 else None
            if m!=slope:
                return False
        return True