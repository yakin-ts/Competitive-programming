# Enter your code here. Read input from STDIN. Print output to STDOUT

englishNum = int(input())
engSet  = set(input().split())
frenchNum = int(input())
frenchSet = set(input().split())

print(len(engSet.difference(frenchSet)))
