# https://leetcode.com/problems/maximal-rectangle/submissions/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def maximalRectangleHistogram(heights):
            stack, ans = [], 0
            for i, h in enumerate(heights+[0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    ans = max(ans, height * width)
                stack.append(i)
            return ans
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        r, c, ans = len(matrix), len(matrix[0]), 0
        row = [0] * c
        for i in range(r):
            for j in range(c):
                row[j] = 0 if matrix[i][j] == '0' else row[j]+1
            ans = max(ans, maximalRectangleHistogram(row))
        return ans
