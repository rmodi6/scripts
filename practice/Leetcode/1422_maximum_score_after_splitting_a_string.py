# https://leetcode.com/contest/weekly-contest-186/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        left_score = 1 if s[0] == '0' else 0
        right_score = sum(map(int, s[1:]))
        max_score = left_score + right_score
        score = max_score
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                score += 1
            else:
                score -= 1
            max_score = max(max_score, score)
        return max_score
