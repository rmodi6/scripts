# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        ans = 0
        p, q = 0, len(people)-1
        while p < q:
            if people[p]+people[q] <= limit:
                p += 1
            elif people[p] >= limit:
                return ans + q - p + 1
            q -= 1
            ans += 1
        return ans + int(p==q)
