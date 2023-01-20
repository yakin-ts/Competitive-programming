class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        #set the bounds for matrix traversal
        upper = -1
        lower = len(matrix)
        left =  -1
        right = len(matrix[0])
        mat_size = len(matrix)*len(matrix[0])
        count_trav = 0
        
        i = upper + 1
        j = left + 1
        while count_trav < mat_size:
            
            #traverse to right
            while   count_trav < mat_size and j < right:
                spiral.append(matrix[i][j])
                j+=1
                count_trav +=1
            upper +=1
            j -=1
            i +=1 

            # Traverse down the matrix
            while   count_trav < mat_size and i < lower :
                spiral.append(matrix[i][j])
                count_trav += 1
                i+=1
            right-=1
            i-=1
            j -=1

            # Traverse to the left
            while count_trav < mat_size and j > left:
                spiral.append(matrix[i][j])
                j-=1
                count_trav +=1
            lower -=1
            j+=1
            i-=1

            # Traverse upwards
            while count_trav < mat_size and i > upper:
                spiral.append(matrix[i][j])
                i-=1
                count_trav +=1
            left +=1
            i+=1
            j+=1
        
        return spiral












