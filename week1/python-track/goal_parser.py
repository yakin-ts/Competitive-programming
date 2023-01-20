class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        last = ''
        isOpen = False
        for char in command:
            if char=='G':
                res += 'G'
            elif char=='(':
                isOpen = True
                last = ''
            elif isOpen and char==')':
                if last =='':
                    res += 'o'
                else:
                    res += last
                    last = ''
                isOpen=False
            else:
                last += char 
        return res