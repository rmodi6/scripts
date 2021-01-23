# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3614/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        
        def sort(i, j):
            diag = []
            x, y = i, j
            while x < r and y < c:
                diag.append(mat[x][y])
                x += 1
                y += 1
            diag = sorted(diag)
            x, y, z = i, j, 0
            while x < r and y < c:
                mat[x][y] = diag[z]
                x += 1
                y += 1
                z += 1
        
        i, j = r-1, 0
        while i >= 0:
            sort(i, j)
            i -= 1
        i, j = 0, 0
        while j < c:
            sort(i, j)
            j += 1
        return mat
