# https://leetcode.com/contest/weekly-contest-185/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        alphas, numbers = [], []
        for c in s:
            if c.isalpha():
                alphas.append(c)
            else:
                numbers.append(c)
        if len(numbers) > len(alphas) + 1 or len(alphas) > len(numbers) + 1:
            return ""
        ans = ''
        if len(alphas) > len(numbers):
            ans += alphas.pop()
            for i in range(len(alphas)):
                ans += numbers[i] + alphas[i]
        elif len(numbers) > len(alphas):
            ans += numbers.pop()
            for i in range(len(alphas)):
                ans += alphas[i] + numbers[i]
        else:
            for i in range(len(alphas)):
                ans += alphas[i] + numbers[i]
        return ans
