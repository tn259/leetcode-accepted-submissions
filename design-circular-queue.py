# we need to maintain an idx which is the frond and an idx which is the back
# when we enqueue the front idx decreases and wraps around
# when we dequeue the back idx increases and wraps around.
# so in the example:

# [,,1]
# [,2,1]
# [3,2,1]
# [3,2,]
# [3,2,4]

class MyCircularQueue:

    def __init__(self, k: int):
        self.buffer = [None] * k
        self.front = k-1
        self.rear = k-1
        self.is_empty = True
        self.is_full = False

    def enQueue(self, value: int) -> bool:
        if self.is_full:
            return False
        newRear = (self.rear - 1) % len(self.buffer) if not self.is_empty else 
            self.rear
        self.buffer[newRear] = value
        self.rear = newRear
        nextRear = (self.rear - 1) % len(self.buffer)
        if self.buffer[nextRear] != None:
            self.is_full = True
        self.is_empty = False
        return True

    def deQueue(self) -> bool:
        if self.is_empty:
            return False
        self.buffer[self.front] = None
        newFront = (self.front - 1) % len(self.buffer)
        if self.buffer[newFront] == None:
            self.is_empty = True
            self.front = self.rear = len(self.buffer)-1
        else:
            self.front = newFront
        self.is_full = False
        print(self.buffer)
        return True
        
    def Front(self) -> int:
        return self.buffer[self.front] if not self.is_empty else -1

    def Rear(self) -> int:
        return self.buffer[self.rear] if not self.is_empty else -1

    def isEmpty(self) -> bool:
        return self.is_empty

    def isFull(self) -> bool:
        return self.is_full


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
