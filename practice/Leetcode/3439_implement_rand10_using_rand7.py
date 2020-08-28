# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3439/

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        evenOrOdd = rand7()
        while evenOrOdd == 7:
            evenOrOdd = rand7()
        isEven = evenOrOdd % 2 == 0
        n = rand7()
        while n > 5:
            n = rand7()
        return n if isEven else n + 5
