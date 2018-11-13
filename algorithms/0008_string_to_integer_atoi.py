"""
1. Get sign
2. If there was a sign, ignore the first character
3. While curr char is a digit, multiply ans by 10 (shift previous digits left)
and add the newest digit
4. Give ans the correct sign
5. Check for overflow
6. Done

"""


class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']:
            s = s[1:]
        ans = 0
        for c in s:
            if not c.isdigit():
                break
            ans *= 10
            ans += int(c)

        ans *= sign
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
        return ans
