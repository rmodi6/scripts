# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, inDegree, ans = defaultdict(set), {}, []
        for prereq in prerequisites:
            graph[prereq[1]].add(prereq[0])
            inDegree[prereq[0]] = inDegree.get(prereq[0], 0) + 1
            
        q = []
        for course in range(numCourses):
            if course not in inDegree:
                q.append(course)
        
        while q:
            course = q.pop()
            ans.append(course)
            for nextCourse in graph[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        return ans if len(ans) == numCourses else []
