# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

class Solution:
    def product_except(self, nums):
        ans = [1] * len(nums)
        
        left = 1
        right = 1
        
        for i in range(len(nums)):
            ans[i] *= left
            # [-1] = last element
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]

        return ans