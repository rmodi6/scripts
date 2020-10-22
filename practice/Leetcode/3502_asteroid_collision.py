# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3502/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = [asteroids[0]]
        for a in asteroids[1:]:
            if a >= 0:
                ans.append(a)
            elif len(ans) > 0:
                if ans[-1] < 0:
                    ans.append(a)
                else:
                    if abs(a) == ans[-1]:
                        ans = ans[:-1]
                    elif abs(a) < ans[-1]:
                        continue
                    else:
                        while len(ans) > 0 and ans[-1] >= 0 and ans[-1] < abs(a):
                            ans = ans[:-1]
                        if len(ans) > 0:
                            if ans[-1] < 0:
                                ans.append(a)
                            elif abs(a) == ans[-1]:
                                ans = ans[:-1]
                            else:
                                continue
                        else:
                            ans.append(a)
            else:
                ans.append(a)
        return ans
