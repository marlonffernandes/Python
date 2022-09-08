# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

class Solution:
    def two_sumv2(self, numbers, target):

        f, b = 0, len(numbers)-1

        while numbers[f]+numbers[b] != target:
            if numbers[f]+numbers[b] > target:
                b -= 1
            else:
                f +=1
        return [f+1,b+1]
