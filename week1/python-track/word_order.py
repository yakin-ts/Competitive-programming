# Enter your code here. Read input from STDIN. Print output to STDOUT

def wordOrder(n):
    d={}
    for i in range(n):
        val = input('')
        if val in d:
            d[val] +=1
        else:
            d[val] = 1
    print(len(d))
    print(*d.values())
    

num = int(input())
wordOrder(num)
        
