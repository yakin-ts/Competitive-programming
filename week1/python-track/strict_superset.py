# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(input().split())
num = int(input())
super_set = True
for _ in range(num):
    tmp = set(input().split())
    if not set_A.issuperset(tmp):
        super_set = False
if not super_set:
    print('False')
else:
    print('True')
