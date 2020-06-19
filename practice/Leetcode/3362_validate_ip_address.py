# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3362/

class Solution:
    def validIPAddress(self, IP: str) -> str:
        exclude = set(list('ghijklmnopqrstuvwxyz'))
        
        splits = IP.split('.')
        if len(splits) == 4:
            for i in splits:
                try:
                    j = int(i)
                except:
                    return 'Neither'
                if i.isalpha() or str(j) != i or j > 255 or j < 0:
                    return 'Neither'
            return 'IPv4'
        splits = IP.lower().split(':')
        if len(splits) == 8:
            for i in splits:
                if len(i) > 4 or not re.search("^([0-9a-f]{1,4})$", i):
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
