# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def group_anagrams(self, strs):
        result = []
        lookup = {}
        for str in strs:
            str_sorted = ''.join(sorted(str))

            if str_sorted not in lookup:
                lookup[str_sorted] = len(result)
                result.append([str])
            else:
                result[lookup[str_sorted]].append(str)
        return result