"""
Create a dict mapping the value of the element in list to index it was seen at.
When you encounter an element whose conjugate (target - el) has been seen,
return the current index and the index of the conjugate.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, el in enumerate(nums):
            if target-el in d:
                return [d[target-el], i]
            else:
                d[el] = i
