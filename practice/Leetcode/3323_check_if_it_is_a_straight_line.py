# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        den = (coordinates[0][0] - coordinates[1][0])
        if den != 0:
            slope = (coordinates[0][1] - coordinates[1][1]) / den
        for i in range(2, len(coordinates)):
            if den == 0:
                if (coordinates[0][0] - coordinates[i][0]) != 0:
                    return False
            else:
                if (coordinates[0][1] - coordinates[i][1]) / (coordinates[0][0] - coordinates[i][0]) != slope:
                    return False
        return True
