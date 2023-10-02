class TrieNode:
    def __init__(self,val):
        self.children = {}
        self.val = val
        # self.is_end


class MapSum:
    def __init__(self):
        self.root = TrieNode(0)
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        if key in self.map:
            for ch in key:
                cur.children[ch].val += ( - self.map[key] + val)
                cur = cur.children[ch]
        else:
            for ch in key:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode(val)
                else:
                    cur.children[ch].val += val
                cur  = cur.children[ch]
        # cur.is_end = True
        self.map[key] = val
                

        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return 0

        return cur.val

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)