# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def two_sum(self, nums, target):
        for i, n in enumerate(nums):
            if target - n in nums[i+1:]:
                nums.remove(n)
                return([i, nums.index(target-n)+1])
