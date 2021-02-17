# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3640/

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        q = [kill]
        ans = []
        hmap = {}
        for i, process in enumerate(ppid):
            hmap[process] = hmap.get(process, []) + [pid[i]]
        while q:
            process = q.pop(0)
            ans.append(process)
            for child in hmap.get(process, []):
                q.append(child)
        return ans
