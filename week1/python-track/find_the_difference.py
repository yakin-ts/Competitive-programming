class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        first = {}
        diff = ""
        
        # populate the dictionary
        for x in t:
            if x not in first:
                first[x] =1
            else:
                first[x] +=1
        # remove the common characters
        for y in s:
            if y not in first:
                first[y] = 1
            else:
                first[y] -= 1
        # identify the difference
        for key, value in first.items():
            if value == 1:
                diff = key
                break
        return diff