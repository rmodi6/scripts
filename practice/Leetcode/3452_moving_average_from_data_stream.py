https://leetcode.com/explore/featured/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3452/

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.sum = 0
        self.arr = []

    def next(self, val: int) -> float:
        self.arr.append(val)
        self.sum += val
        if len(self.arr) > self.size:
            self.sum -= self.arr.pop(0)
        return self.sum / len(self.arr)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
