# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3648/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        possible = set(range(n))
        while possible:
            print(possible)
            e = next(iter(possible))
            remove = set()
            for o in possible:
                if e != o:
                    if not knows(e, o):
                        remove.add(o)
                    else:
                        remove.add(e)
            possible -= remove
            if e in possible:
                for o in range(n):
                    if e != o and (not knows(o, e) or knows(e, o)):
                        return -1
                return e
        return -1
