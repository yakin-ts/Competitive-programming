class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_word = words[0]
        comm = {}
        result = []

        for c in first_word:
            if c in comm:
                comm[c] +=1
            else:
                comm[c] = 1
                
            
        for i,word in  enumerate(words):
            if i!=0:
                for key, value in comm.items():
                    if key in word:
                        count = word.count(key)
                        comm[key] = min(value,count)
                    else:
                        comm[key] = 0
        
        for key, value in comm.items():
            tmp = [key]*value
            result.extend(tmp)
        return result

            

                
                