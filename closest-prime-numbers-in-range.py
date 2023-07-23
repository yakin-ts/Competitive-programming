class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(x):
            for i in range(2,int((x)**0.5)+1):
                if x%i==0:
                    return False
            return True
        
        def diff(x,y,df):
            return 0 < (y-x) < df
        
        result = [-1,-1]
        flag = False
        run_diff = inf
        while left < right+1:
            if isPrime(left):
                for j in range(left+1, right+1):
                    if isPrime(j):
                        flag = True
                        break
                if flag and diff(left,j,run_diff)and left >= 2:
                        result = [left, j]
                        run_diff = j - left
                        left = j
                else: left += 1
            else: left+=1
            if 1<= run_diff <=2:
                break
        return result