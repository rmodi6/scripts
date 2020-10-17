# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3497/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rh, ch = len(matrix)-1, len(matrix[0])-1
        rl, cl = 0, 0
        while rl <= rh:
            rm = rl + (rh-rl)//2
            if matrix[rm][cl] == target:
                return True
            elif matrix[rm][cl] > target:
                rh = rm - 1
            elif matrix[rm][cl] < target and (rm+1 >= len(matrix) or matrix[rm+1][cl] > target):
                break
            else:
                rl = rm + 1
        if target < matrix[rm][cl] or target > matrix[rm][ch]:
            return False
        while cl <= ch:
            cm = cl + (ch-cl)//2
            if matrix[rm][cm] == target:
                return True
            elif matrix[rm][cm] > target:
                ch = cm - 1
            else:
                cl = cm + 1
        return False
