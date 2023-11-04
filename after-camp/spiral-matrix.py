class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []
        top = -1
        bottom = len(matrix)
        left = -1
        right = len(matrix[0])
        size = bottom*right
        count = 0
        
        i = top + 1
        j = left + 1
        while count < size:
            while count < size and j < right:
                ans.append(matrix[i][j])
                j+=1
                count +=1
            top +=1
            j-=1
            i+=1

            while count < size and i < bottom:
                ans.append(matrix[i][j])
                i+=1
                count  += 1
            right -=1
            i-=1
            j-=1

            while count < size and j > left:
                ans.append(matrix[i][j])
                count +=1
                j-=1
            bottom -=1
            j+=1
            i-=1

            while count < size and i > top:
                ans.append(matrix[i][j])
                count +=1
                i-=1
            left +=1
            i+=1
            j+=1

        return ans


        