# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3696/

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k + 1
        self.q = [-1]*self.k
        self.f = self.r = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q[self.r] = value
            self.r = (self.r + 1) % self.k
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.q[self.f] = -1
            self.f = (self.f + 1) % self.k
            return True
        return False

    def Front(self) -> int:
        return self.q[self.f]

    def Rear(self) -> int:
        return self.q[self.r - 1]

    def isEmpty(self) -> bool:
        return self.f == self.r

    def isFull(self) -> bool:
        return (self.r + 1) % self.k == self.f


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
