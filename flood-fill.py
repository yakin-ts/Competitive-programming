class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R = len(image)
        C = len(image[0])
        start_color = image[sr][sc]
       

        def dfs(row,col):
            if not (0<=row<R and 0<=col<C) or image[row][col]==color:
                return
            if image[row][col] == start_color:
                image[row][col] = color
                dfs(row-1,col)
                dfs(row,col-1)
                dfs(row+1,col)
                dfs(row,col+1)
                    
        
        dfs(sr,sc)

        return image