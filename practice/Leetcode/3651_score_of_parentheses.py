# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                temp = 1
                while stack[-1] != '(':
                    temp = 2*stack.pop()
                stack.pop()
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack.append(temp)
        return stack[-1]
