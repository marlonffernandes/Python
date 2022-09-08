# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

class Solution:
    def palindrome(self, s):
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        return s == s[::-1]