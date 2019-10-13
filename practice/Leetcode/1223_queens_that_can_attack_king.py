# https://leetcode.com/contest/weekly-contest-158/problems/queens-that-can-attack-the-king/

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        pos = []
        kx, ky = king[0], king[1]
        queen_pos = set()
        for q in queens:
            queen_pos.add((q[0], q[1]))
        for y in range(ky + 1, 8):
            if (kx, y) in queen_pos:
                pos.append([kx, y])
                break
        for y in range(ky - 1, -1, -1):
            if (kx, y) in queen_pos:
                pos.append([kx, y])
                break
        for x in range(kx + 1, 8):
            if (x, ky) in queen_pos:
                pos.append([x, ky])
                break
        for x in range(kx - 1, -1, -1):
            if (x, ky) in queen_pos:
                pos.append([x, ky])
                break
        x, y = kx - 1, ky + 1
        while x > -1 and y < 8:
            if (x, y) in queen_pos:
                pos.append([x, y])
                break
            x -= 1
            y += 1
        x, y = kx + 1, ky + 1
        while x < 8 and y < 8:
            if (x, y) in queen_pos:
                pos.append([x, y])
                break
            x += 1
            y += 1
        x, y = kx + 1, ky - 1
        while x < 8 and y > -1:
            if (x, y) in queen_pos:
                pos.append([x, y])
                break
            x += 1
            y -= 1
        x, y = kx - 1, ky - 1
        while x > -1 and y > -1:
            if (x, y) in queen_pos:
                pos.append([x, y])
                break
            x -= 1
            y -= 1
        return pos
