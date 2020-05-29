# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3344/

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def isCycle(course, prereqs, visited, path):
            if visited[course]:
                return False
            if path[course]:
                return True
            
            path[course] = True
            
            ans = False
            for child in prereqs[course]:
                if isCycle(child, prereqs, visited, path):
                    ans = True
                    break
            
            path[course] = False
            visited[course] = True
            
            return ans
        
        prereqs = defaultdict(list)
        for p in prerequisites:
            prereqs[p[1]] += [p[0]] 
        visited = [False for i in range(numCourses)]
        path = [False for i in range(numCourses)]
        
        for course in range(numCourses):
            if isCycle(course, prereqs, visited, path):
                return False
        return True
