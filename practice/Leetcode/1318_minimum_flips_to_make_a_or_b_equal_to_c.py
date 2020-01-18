# https://leetcode.com/contest/weekly-contest-171/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bin_a = bin(a).replace("0b", "")
        bin_b = bin(b).replace("0b", "")
        bin_c = bin(c).replace("0b", "")
        max_len = max([len(bin_a), len(bin_b), len(bin_c)])
        while len(bin_a) < max_len:
            bin_a = '0' + bin_a
        while len(bin_b) < max_len:
            bin_b = '0' + bin_b
        while len(bin_c) < max_len:
            bin_c = '0' + bin_c
        ans = 0
        for i in range(max_len):
            x, y, z = int(bin_a[i]), int(bin_b[i]), int(bin_c[i])
            if (x | y) == z:
                continue
            elif (((1-x) | y) == z) or ((x | (1-y)) == z):
                ans += 1
            else:
                ans += 2
        return ans