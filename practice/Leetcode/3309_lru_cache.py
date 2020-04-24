# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3309/

from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.c = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if len(self) >= self.c and key not in self:
            self.popitem(last = False)
        if key in self:
            self.move_to_end(key)
        self[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
