# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334/

class StockSpanner:

    def __init__(self):
        self.dp = []

    def next(self, price: int) -> int:
        if len(self.dp) == 0:
            self.dp.append((price, 1, 0))
        else:
            previous = self.dp[-1]
            if previous[0] > price:
                self.dp.append((price, 1, len(self.dp)))
            else:
                span = 1
                while previous[0] <= price:
                    span += previous[1]
                    index = previous[2]
                    if index == 0:
                        break
                    previous = self.dp[index - 1]
                self.dp.append((price, span, index))
        return self.dp[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)