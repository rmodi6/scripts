# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        visited = [[False for j in range(len(image[0]))] for i in range(len(image))]
        self.recursion(image, visited, sr, sc, oldColor, newColor)
        return image
    
    def recursion(self, image, visited, i, j, oldColor, newColor):
        if i >= 0 and i < len(image) and j >= 0 and j < len(image[0]) and not visited[i][j] and image[i][j] == oldColor:
            image[i][j] = newColor
            visited[i][j] = True
            self.recursion(image, visited, i-1, j, oldColor, newColor)
            self.recursion(image, visited, i+1, j, oldColor, newColor)            
            self.recursion(image, visited, i, j-1, oldColor, newColor)            
            self.recursion(image, visited, i, j+1, oldColor, newColor)
