# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379/

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N > 14:
            N = N%14
        if N == 0:
            N = 14
        for i in range(N):
            nextcells = [0] * 8
            for j in range(1, 7):
                if cells[j-1] == cells[j+1]:
                    nextcells[j] = 1
                else:
                    nextcells[j] = 0
            nextcells[0], nextcells[-1] = 0, 0
            cells = nextcells
            
        return cells
