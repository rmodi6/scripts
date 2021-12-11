# https://leetcode.com/problems/jump-game-iii/submissions/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        return self.canReachUtil(arr, start, visited)

    def canReachUtil(self, arr, i, visited):
        if i in visited or i < 0 or i >= len(arr):
            return False
        if arr[i] == 0:
            return True
        visited.add(i)
        return self.canReachUtil(arr, i - arr[i], visited) or self.canReachUtil(arr, i + arr[i], visited)
