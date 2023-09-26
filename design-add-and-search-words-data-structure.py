class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for chr in word:
            if chr not in cur.children:
                cur.children[chr] = TrieNode()
            cur = cur.children[chr]
        cur.is_end = True
    
        
        
    def search(self, word: str) -> bool:
        cur = self.root
        return self.dfs(cur, word)
        
    def dfs(self, node, word):
        if not word:
            return node.is_end
        if word[0] == '.':
            for child in node.children.values():
                if self.dfs(child, word[1:]):
                    return True
        else:
            child = node.children.get(word[0])
            if child:
                return self.dfs(child, word[1:])
        return False


       
        

                
   
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)