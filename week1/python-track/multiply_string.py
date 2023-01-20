class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        num1_int =0
        num2_int = 0

        for i,n in enumerate(reversed(num1)):
            num1_int += ((ord(n) - ord('0'))*(10**i)) 

        for j,m in enumerate(reversed(num2)):
            num2_int += ((ord(m) - ord('0'))*(10**j))

        product = num1_int * num2_int
        return str(product)