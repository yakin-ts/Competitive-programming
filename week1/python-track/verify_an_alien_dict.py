class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d= {}
        for i, l in enumerate(order):
            d[l] = i

        leng = len(words)
        i=0
        while i < leng-1:
            word1 = words[i]
            word2 = words[i+1]
            j=0
            s_len = len(word1)
            # done = False

            while j < s_len:
                # print(word1[j],word2[j])
                if d[word1[j]] < d[ word2[j]]:
                    # return True
                    break
                if j+1 == (len(word2)) and len(word1) > len(word2):
                    print('before')
                    return False
                if d[word1[j]] > d[word2[j]]:
                    return False
                
                j+=1
            i+=1
        return True


        