"""
A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of
ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

cache = {}


class Solution:
    """
    Facts:

    - Any string that has a digit > 2 right before a 0 has 0 possibilities.
    This is because neither {3-9}0 nor anything starting with 0 are valid.
    - Any string starting with a zero is invalid, return 0
    - Any number of length 2 has two possibilities if it is <= 26 and not 10 or
      20. Otherwise it only has one possibility
    - Any non-zero digit has 1 possibility

    Resursive intuition:
    - We decide how to recurse based on first two digits of the string.  
    - If it is <= 26 and not in [10, 20], it has the number of possibilities of
      substring s[1:] + s[2:]
    - If it is 10 or 20 it has the same number of possibilities as the substring
      starting at index 2 - s[2:]
    - Otherwise it has the same number of possibilities as the substring
      starting at index 1 - s[1:]

    For all of these calls, we will have significant overlap in the substrings
    we look at.  For that reason, we use a cache/dp to store the results for 
    future lookup.  Before we do any recursive calls, we check the cache to see
    if we can return a value immediately.
    """

    def helper(self, s):
        global cache
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            d = int(s)
            return 2 if d <= 26 and s[1] != '0' else 1
        if s in cache:
            return cache[s]
        else:
            top = int(s[:2])
            if top <= 26:
                cache[s] = self.helper(s[1:]) + self.helper(s[2:])
            else:
                cache[s] = self.helper(s[1:])
            return cache[s]

    def numDecodings(self, s):
        global cache
        for i in range(len(s) - 1):
            if s[i] > '2' and s[i + 1] == '0':
                return 0
        ans = self.helper(s)
        cache = {}
        return ans
