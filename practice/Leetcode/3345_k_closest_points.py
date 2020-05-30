# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def distanceToOrigin(point):
            return (point[0]**2 + point[1]**2) ** 0.5
        
        distanceToPointMap = {}
        
        for point in points:
            d = distanceToOrigin(point)
            l = distanceToPointMap.get(d, [])
            l.append(point)
            distanceToPointMap[d] = l
        
        ans = []
        for d in sorted(distanceToPointMap.keys()):
            ans.extend(distanceToPointMap[d])
            if len(ans) >= K:
                break
                
        return ans
