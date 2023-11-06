class Solution:
    def isMatch(self, s, p):
        memo = {}

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                result = (i == len(s))
            else:
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j + 1 < len(p) and p[j + 1] == '*':
                    result = (solve(i, j + 2) or (first_match and solve(i + 1, j)))
                else:
                    result = first_match and solve(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return solve(0, 0)
