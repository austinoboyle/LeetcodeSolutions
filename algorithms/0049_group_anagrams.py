"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class AnagramObject(object):
    def __init__(self, s):
        self.actual = s
        self.sorted = ''.join(sorted(s))


class Solution(object):
    """
    Intuition: 2 strings are each other's anagrams iff their chars in sorted
    order are equal.

    Use simple AnagramObject class to abstract away the string sorting.

    Maintain a dict mapping unique sorted strings to actual strings in the arr
    Loop through each of these AnagramObjects, updating the dict for each by
    either creating a new key or appending to an existing value.

    The groups of anagrams are the final dict's values.
    """

    def groupAnagrams(self, strs):
        objects = map(AnagramObject, strs)
        groups = {}
        for o in objects:
            if o.sorted in groups:
                groups[o.sorted].append(o.actual)
            else:
                groups[o.sorted] = [o.actual]

        return groups.values()
