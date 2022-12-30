# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

nums  = tuple(map(int,input().split()))
n , m = nums
def def_value():
    return -1
grp_a = defaultdict(list)

for i in range(n):
    x = input()
    grp_a[x].append(i+1)
for _ in range(m):
    x = grp_a[input()]
    print(*x) if x else print(-1)

