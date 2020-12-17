# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3569/

class Solution:
    
    def make_combs(self, X, Y):
        combs = collections.defaultdict(int)
        for x in X:
            for y in Y:
                combs[x + y] += 1
        
        return combs
        
    
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        combs_AB = self.make_combs(A, B)
        combs_CD = self.make_combs(C, D)
        
        total = 0
        for comb1, count1 in combs_AB.items():
            total += count1 * combs_CD[-comb1]
                
        return total
