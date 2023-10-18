class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.items= []
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set[val] = len(self.items)
            self.items.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        last = self.items[-1]
        self.items[self.set[val]] = last
        self.set[last] = self.set[val]
        self.items.pop()
        del self.set[val]
        return True
        
        

    def getRandom(self) -> int:
        return random.choice(self.items)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()