class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if n > 0:
                stack.append(n)
            else:
                while stack and stack[-1] > 0:
                    top = stack.pop()
                    coll = top + n

                    if coll > 0:
                        stack.append(top)
                        break
                    elif coll==0:
                        break
                else:
                    stack.append(n)
        return stack
