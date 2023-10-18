class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a','e','i','o','u'}
        cnt = 0
        n = len(word)
        for i,ch in enumerate(word):
            if ch in vowels:
                cnt += (n-i)*(i+1)
        return cnt