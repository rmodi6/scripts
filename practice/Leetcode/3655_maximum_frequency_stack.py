# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3655/

class FreqStack:

    def __init__(self):
        self.freq = {}
        self.heap = []
        self.t = 0

    def push(self, x: int) -> None:
        self.freq[x] = self.freq.get(x, 0) + 1
        heapq.heappush(self.heap, (-self.freq[x], -self.t, x))
        self.t += 1

    def pop(self) -> int:
        f, t, x = heapq.heappop(self.heap)
        self.freq[x] -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
