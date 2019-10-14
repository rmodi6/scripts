# https://leetcode.com/problems/prime-palindrome/

class Solution:
    def primePalindrome(self, N: int) -> int:
        
        def isPrime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        for D in range(1, 6):
            left = 10 ** (D-1)
            while left < 10 ** D:
                left_str = str(left)
                i = D - 2
                right_str = ''
                while i >= 0:
                    right_str += left_str[i]
                    i -= 1
                palindrome = int(left_str + right_str)
                if palindrome >= N and isPrime(palindrome):
                    return palindrome
                left += 1
            left = 10 ** (D-1)
            while left < 10 ** D:
                left_str = str(left)
                i = D - 1
                right_str = ''
                while i >= 0:
                    right_str += left_str[i]
                    i -= 1
                palindrome = int(left_str + right_str)
                if palindrome >= N and isPrime(palindrome):
                    return palindrome
                left += 1
