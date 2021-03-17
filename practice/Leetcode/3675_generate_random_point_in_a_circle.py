# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3675/

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self._x = x_center
        self._y = y_center
        self.area = math.pi * radius ** 2

    def randPoint(self) -> List[float]:
        theta = 2 * math.pi * random.random()
        R = math.sqrt(random.uniform(0, self.area) / math.pi)
        return [self._x + R * math.cos(theta), self._y + R * math.sin(theta)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
