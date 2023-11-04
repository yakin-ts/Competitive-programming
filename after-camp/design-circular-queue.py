class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [None]*k
        self.head = -1
        self.tail = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.head == -1 or self.tail==-1:
            self.head +=1
            self.tail +=1
            self.que[self.tail] = value
            return True
        else:
            if (self.tail + 1)%self.size is not self.head:
                self.tail = (self.tail+1)%self.size 
                self.que[self.tail] = value
                return True
            else:
                return False
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.head is not -1:
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
                return True
            else:
                self.head = (self.head +1)%self.size
                return True
    def Front(self) -> int:
        return self.que[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.que[self.tail] if not self.isEmpty() else -1
        

    def isEmpty(self) -> bool:
        return self.head is -1

    def isFull(self) -> bool:
        return ((self.tail+1)%self.size ) is self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()