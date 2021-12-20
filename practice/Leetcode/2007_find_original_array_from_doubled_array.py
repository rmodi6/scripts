# https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2:
            return []
        hmap = {}
        ans = []
        for n in sorted(changed):
            if n%2==0 and n//2 in hmap:
                ans.append(n//2)
                hmap[n//2] -= 1
                if hmap[n//2] == 0:
                    del hmap[n//2]
            else:
                hmap[n] = hmap.get(n, 0) + 1

        return ans if  len(hmap)==0 else []
