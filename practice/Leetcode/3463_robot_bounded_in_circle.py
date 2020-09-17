# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos, dir = [0, 0], 0
        curr_pos, curr_dir = pos, dir
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for _ in range(4):
            for instr in instructions:
                if instr == 'G':
                    curr_pos = list(map(sum, zip(curr_pos, directions[curr_dir])))
                elif instr == 'L':
                    curr_dir = (curr_dir-1) % 4
                else:
                    curr_dir = (curr_dir+1) % 4
            if curr_pos == pos and curr_dir == dir:
                return True
        return False
