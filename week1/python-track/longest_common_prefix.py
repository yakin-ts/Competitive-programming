class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sliced_col = zip(*strs)
        commonPrefix = ''
        for cols in sliced_col:
            if len(set(cols)) is 1:
                commonPrefix += cols[0]
            else:
                break
        return commonPrefix
