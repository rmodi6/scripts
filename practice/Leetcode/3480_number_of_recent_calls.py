# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/

class RecentCounter:

    def __init__(self):
        self.dp = []
        self.p = -1

    def ping(self, t: int) -> int:
        if len(self.dp) == 0:
            self.dp.append(t)
            self.p = 0
            return 1
        else:
            while self.p < len(self.dp) and t - 3000 > self.dp[self.p]:
                self.p += 1
            self.dp.append(t)
            return len(self.dp) - self.p


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
