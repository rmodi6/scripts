# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3663/

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [-1] * 10000
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash = key % 10000
        if self.arr[hash] == -1:
            self.arr[hash] = [[key, value]]
        else:
            flag = True
            for i, li in enumerate(self.arr[hash]):
                k, v = li
                if key == k:
                    self.arr[hash][i] = [key, value]
                    flag = False
                    break
            if flag:
                self.arr[hash].append([key, value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash = key % 10000
        if self.arr[hash] == -1:
            return -1
        else:
            for i, li in enumerate(self.arr[hash]):
                k, v = li
                if key == k:
                    return v
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash = key % 10000
        if self.arr[hash] == -1:
            return
        else:
            toRemove = -1
            for i, li in enumerate(self.arr[hash]):
                k, v = li
                if key == k:
                    toRemove = i
                    break
            if toRemove == -1:
                return
            del self.arr[hash][toRemove]
            if len(self.arr[hash]) == 0:
                self.arr[hash] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)