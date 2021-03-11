# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3667/

class Solution:
    def intToRoman(self, num: int) -> str:
        hmap = {1   : {1: 'I', 5: 'V'},
                10  : {10: 'X', 50: 'L'},
                100 : {100: 'C', 500: 'D'},
                1000: {1000: 'M'}}
        special = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        i = 1
        ans = ''
        while num != 0:
            d = (num % 10)*i
            if d in special:
                ans = special[d] + ans
            else:
                temp = ''
                for k in sorted(hmap[i].keys(), reverse=True):
                    while d >= k:
                        temp = temp + hmap[i][k]
                        d = d - k
                ans = temp + ans
            num = num // 10
            i = i * 10
        return ans
