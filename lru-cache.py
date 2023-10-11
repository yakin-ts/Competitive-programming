class LRUCache:

    def __init__(self, capacity: int):
        self.recents = deque([])
        self.cap = capacity
        self.count = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        num = self.cache[key]
        if self.recents and self.recents[-1] != key:
            self.recents.remove(key)
            self.recents.append(key)
        return num

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.recents.remove(key)
            self.recents.append(key)
        else:
            if self.count < self.cap:
                self.cache[key] = value
                self.count += 1
                self.recents.append(key)
            else:
                least = self.recents.popleft()
                while least not in self.cache:
                    least = self.recents.popleft()
                del self.cache[least]
                self.cache[key] = value
                self.recents.append(key)