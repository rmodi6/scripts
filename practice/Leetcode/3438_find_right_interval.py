# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3438/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:
            return []
        
        def binary_search(arr, target):
            l, h = 0, len(arr) - 1
            while l <= h:
                mid = l + (h-l) // 2
                if arr[mid] == target:
                    return target
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            if arr[l] >= target:
                return arr[l]
            else:
                return arr[l+1]
        
        bst = []
        hmap = {}
        for i, interval in enumerate(intervals):
            start, end = interval
            bst.append(start)
            hmap[start] = i
        bst = sorted(bst)
        _max, _min = bst[-1], bst[0]
        ans = []
        for start, end in intervals:
            if end in hmap:
                ans.append(hmap[end])
            elif end > _max:
                ans.append(-1)
            elif end <= _min:
                ans.append(hmap[_min])
            else:
                val = binary_search(bst, end)
                ans.append(hmap.get(val, -1))
        return ans
