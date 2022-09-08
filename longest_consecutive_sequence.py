# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. Must run in O(N)

def longest_consecutive(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best