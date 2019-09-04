# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    
    alphabets = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        return self.getCombinations(digits, 0, "")

    def getCombinations(self, digits, i, currentCombination):
        if i >= len(digits):
            return [currentCombination]
        answer = []
        letters = self.alphabets[digits[i]]
        for letter in letters:
            combination = currentCombination + letter
            answer.extend(self.getCombinations(digits, i+1, combination))
        return answer
