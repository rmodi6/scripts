# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391/

import re

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(re.split('\s+', s.strip())[::-1])
