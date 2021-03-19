# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3677/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        keys = set([0])
        queue = [0]
        while queue and len(keys) < len(rooms):
            key = queue.pop(0)
            visited.add(key)
            other_keys = set(rooms[key])
            keys.update(other_keys)
            queue += list(other_keys - visited)
        return len(keys) == len(rooms)
