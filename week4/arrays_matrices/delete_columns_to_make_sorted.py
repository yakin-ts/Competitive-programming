class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        del_count = 0
        last_char = -1

        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if last_char==-1:
                    last_char = ord(strs[j][i])
                else:
                    if last_char <= ord(strs[j][i]):
                        last_char = ord(strs[j][i])
                    else:
                        del_count +=1
                        break
            last_char = -1
        return del_count