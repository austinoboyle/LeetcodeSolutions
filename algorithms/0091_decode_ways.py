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
    Use dynamic programming to store number of possibilities for strings ending
    at index i.  Possibilities for ending at one index depends on the length 1
    and 2 ints ending at that index, and possibilities for ending at previous
    indices. 
    """

    def numDecodings(self, s):
        N = len(s)
        pre_prev = 1
        prev = 0 if s[0] == '0' else 1
        for i in range(2, N+1):
            newP = 0
            first = int(s[i-1])
            second = int(s[i-2:i])
            if first > 0:
                newP += prev
            if second >= 10 and second <= 26:
                newP += pre_prev
            pre_prev, prev = prev, newP
        return prev
