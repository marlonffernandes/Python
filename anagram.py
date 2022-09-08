#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def anagram(self, s, t):
        return(sorted(s) == sorted(t))