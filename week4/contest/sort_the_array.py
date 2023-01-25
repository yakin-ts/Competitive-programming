import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

def sort_the_array(arr):
    if len(arr) <= 1:
        print('yes')
        return
    
    left = -1
    right = 0
    t_left = 
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            if left < -1:
                left = i
            t_left = i
            right = i+1
        else:
            if left != -1:
                if arr[left] > arr[i+1]:
                    print('no')
                    return
                else:
                    left = i+1
    print('yes')
                    
                
    
    
             