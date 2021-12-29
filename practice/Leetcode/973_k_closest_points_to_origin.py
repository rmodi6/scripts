# https://leetcode.com/problems/k-closest-points-to-origin

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

# One liner

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda point: (point[0]**2 + point[1]**2)**0.5)[:k]
