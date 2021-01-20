# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3610/

class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i, c in enumerate(s):
            if c in hmap:
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False
                pc = stack.pop()
                if hmap[pc] != c:
                    return False
        return len(stack) == 0
