# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.maxLengthUtil(arr, 0, set(), 0)
    
    def maxLengthUtil(self, arr, i, result, ans):
        if i >= len(arr):
            return len(result)
        
        chars = set(arr[i])
        if len(chars) == len(arr[i]):
            ans1 = self.maxLengthUtil(arr, i+1, result, ans)
            ans2 = 0
            if len(chars.intersection(result)) == 0:
                ans2 = self.maxLengthUtil(arr, i+1, chars.union(result), ans)
            return max(ans, ans1, ans2)
        else:
            return self.maxLengthUtil(arr, i+1, result, ans)
