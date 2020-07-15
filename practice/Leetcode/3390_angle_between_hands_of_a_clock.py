# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3390/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minAngle = 6*minutes
        hourAngle = 30*hour+0.5*minutes
        if hourAngle > minAngle:
            return min(hourAngle - minAngle, 360 - hourAngle + minAngle)
        else:
            return min(minAngle - hourAngle, 360 - minAngle + hourAngle)
