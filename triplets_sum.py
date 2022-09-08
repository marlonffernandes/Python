
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# len(nums)-2 is because we need at least 3 numbers to continue.
# if i > 0 and nums[i] == nums[i-1] is because when i = 0, it doesn't need to check if it's a duplicate element since it doesn't even have a previous element to compare with. And nums[i] == nums[i-1] is to prevent checking duplicate again. (This seems to be a good pattern which has been seen in other questions as well).


class Solution:

    def three_sum(self, nums):
        nums.sort()
        result = []
        # renamed this to left because this will always be the leftmost pointer in the triplet
        for left in range(len(nums) - 2):
            # this step makes sure that we do not have any duplicates in our result output
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid = left + 1  # renamed this to mid because this is the pointer that is between the left and right pointers
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0:
                    mid += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    # Another conditional for not calculating duplicates
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    # Avoiding duplicates check
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return result
