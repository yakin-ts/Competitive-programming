class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(arr,cl,op):
            if n==cl and n==op:
                res.append("".join(arr))
            elif n == op:
                arr.append(')')
                backtrack(arr,cl+1,op)
                arr.pop()
            else:
                arr.append('(')
                backtrack(arr,cl,op+1)
                arr.pop()
                
                if op > cl:
                    arr.append(')')
                    backtrack(arr,cl+1,op)
                    arr.pop()
        backtrack([],0,0)

        return res

                    


        