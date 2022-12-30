# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import Counter
def capsRoom(k,rooms):
    d={}
    for i in rooms:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
    for k,v in d.items():
        if v is 1:
            print(k)
            break
    # print(sorted(d.items(), key=lambda x:x[1])[0][0])

k = int(input())
rooms = list(in)
 
capsRoom(k,rooms)
