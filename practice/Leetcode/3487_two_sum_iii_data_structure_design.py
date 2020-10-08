# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3487/

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hset = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.hset[number] = self.hset.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.hset:
            if (value-n) in self.hset:
                if (value-n) != n:
                    return True
                elif self.hset[n] > 1:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
