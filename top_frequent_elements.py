# Given an integer array nums and an integer k, return the k most frequent elements.

from collections import Counter

class Solution:
    def top_frequent(self, nums, k):
        c = Counter(nums)
        # get every key in the list and construct a list out of it. This feature belongs to regEx parsing [*c]
        return sorted([*c], key=c.get, reverse=True)[:k]
