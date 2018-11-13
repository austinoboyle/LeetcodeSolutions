"""
1. Get the sign of x, then convert it to its abs value
2. While x is not 0, multiply ans by 10 (shift all digits left 1), and add the
   last digit of x.
3. Change ans back to correct sign
4. Check if ans is outside integer boundaries
5. Return ans
   EXAMPLE: x = 321
    i. ans = 0, ans = 1, x = 32
    ii. ans = 10, ans = 12, x = 3
    iii. ans = 120, ans = 123, x = 0
    return 123
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -(1 << 31)
        INT_MAX = (1 << 31) - 1
        sign = -1 if x < 0 else 1
        x *= sign

        ans = 0
        while x:
            ans *= 10
            ans += x % 10
            x //= 10
        ans *= sign
        if ans < INT_MIN or ans > INT_MAX:
            return 0
        return ans
