# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3664/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hmap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        ans = ''
        for n in num:
            if n not in hmap:
                return False
            ans = hmap[n] + ans
        return ans == num
