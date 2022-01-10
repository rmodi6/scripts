# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, summ, carry = len(a) - 1, len(b) - 1, "", 0
        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0
            summ += str((d1 + d2 + carry) % 2)
            carry = (d1 + d2 + carry) // 2
            i, j = i-1, j-1 
        return summ[::-1]

# One liner
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
