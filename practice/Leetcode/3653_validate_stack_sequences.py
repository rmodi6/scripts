# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3653/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        indices = [pushed.index(n) for n in popped]
        visited = set()
        prev = -1
        for i in indices:
            visited.add(i)
            while prev > i:
                if prev not in visited:
                    return False
                prev -= 1
            prev = i
        return True
