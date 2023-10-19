class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x_axis = 0
        y_axis = 0
        direction = ['n','e','s','w']
        idx = 0
        dirn = 'n'
        for ch in instructions:

            if ch=='G':
                if dirn=='n':
                    y_axis +=1
                elif dirn=='s':
                    y_axis -=1
                elif dirn=='e':
                    x_axis +=1
                else:
                    x_axis -=1
            elif ch=='L':
                idx -= 1
                dirn = direction[idx%4]
            else:
                idx += 1
                dirn = direction[idx%4]
        return dirn!='n' or (x_axis==0 and y_axis==0)