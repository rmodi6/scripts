# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3506/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = sorted(tokens)
        if len(tokens) == 0 or P < tokens[0]:
            return 0
        ans = score = 0
        i, j = 0, len(tokens)-1
        while i <= j:
            if tokens[i] <= P:
                P -= tokens[i]
                score += 1
                ans = max(ans, score)
                i += 1
            elif score > 0:
                P += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return ans
