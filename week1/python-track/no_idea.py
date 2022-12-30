# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m = list(map(int,input().split()))
nums = list(map(int,input().split()))
m_a = set(map(int,input().split()))
m_b = set(map(int,input().split()))
happiness = 0

def happiness(nums,a,b):
    happy = 0
    for item in nums:
        if item in a:
            happy +=1
        elif item in b:
            happy -=1
    print(happy)
happiness(nums,m_a,m_b)
