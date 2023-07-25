class Solution:
    def maxProduct(self, words: List[str]) -> int:
        alph = {
            'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32, 'g': 64, 'h': 128,
            'i': 256, 'j': 512, 'k': 1024, 'l': 2048, 'm': 4096, 'n': 8192, 'o': 16384,
            'p': 32768, 'q': 65536, 'r': 131072, 's': 262144, 't': 524288, 'u': 1048576,
            'v': 2097152, 'w': 4194304, 'x': 8388608, 'y': 16777216, 'z': 33554432
        }

        def bitman(wrd):
            res = 0
            for c in wrd:
                res |= alph[c]
            return res

        max_length = {}
        for word in words:
            bm = bitman(word)
            max_length[bm] = max(max_length.get(bm, 0), len(word))

        max_prod = 0
        for bm1, len1 in max_length.items():
            for bm2, len2 in max_length.items():
                if bm1 & bm2 == 0:
                    max_prod = max(max_prod, len1 * len2)

        return max_prod