# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3301/

class Solution:
    def checkValidString(self, s: str) -> bool:
        star_indexes = []
        stack = []
        for i, c in enumerate(s):
            if c == '*':
                star_indexes.append(i)
            elif c == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                elif len(star_indexes) > 0:
                    star_indexes.pop()
                else:
                    return False
        while len(stack) > 0:
            i = stack.pop()
            if len(star_indexes) == 0:
                return False
            j = star_indexes.pop()
            if j < i:
                return False
        return True
