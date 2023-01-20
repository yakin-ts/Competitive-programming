import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n = list(map(int, input().split()))
    chess = []
    for _ in range(m):
        row = list(map(int, input().split()))
        chess.append(row)
    right_sum = [[chess[i][j] for j in range(len(chess[0]))] for i in range(len(chess))]
    left_sum = [[chess[i][j] for j in range(len(chess[0]))] for i in range(len(chess))]

    
    
    # Build prefix sum diagonally towards right
    for i in range(m):
        k = i
        j=0
        last = 0
        while k < m and j < n:
            right_sum[k][j] +=last
            last = right_sum[k][j]
            k+=1
            j+=1
                
    for j in range(1,n):
        k = j
        l =0
        last = 0
        while k < n and l < m:
            right_sum[l][k] +=last
            last = right_sum[l][k]
            k+=1
            l+=1
    
    # Build prefix sum diagonally towards left
    for i in range(m):
        k = i
        j=n-1
        last = 0
        while k < m and j > -1:
            left_sum[k][j] +=last
            last = left_sum[k][j]
            k+=1
            j-=1
    for j in range(n-2,-1,-1):
        k = j
        l = 0 
        last = 0
        while k > -1 and l < m:
            left_sum[l][k] +=last
            last = left_sum[l][k]
            k-=1
            l+=1
    
    max_diag = 0
    for i in range(chess):
        for j in range(chess[i]):
            tmp = 
    
    