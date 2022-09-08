#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def contains_duplicate(self, nums):
        return(len(nums) != len(set(nums)))
