# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31-1
        sign = 1
        str = str.strip()
        if str == '':
            return 0
        if (str[0] != '-' and str[0] != '+' and not str[0].isdigit()):
            return 0
        if str[0] == '+' or str[0] == '-':
            sign = -1 if str[0] == '-' else 1
            str = str[1:]
        if str == '' or not str[0].isdigit():
            return 0
        number, i = '', 0
        while i < len(str) and str[i].isdigit():
            number += str[i]
            i += 1
        number = sign * int(number)
        return min(max(number, INT_MIN), INT_MAX)
