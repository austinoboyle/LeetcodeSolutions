"""
Given two integers dividend and divisor, divide two integers without using
multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3 Output: 3 Example 2:

Input: dividend = 7, divisor = -3 Output: -2 

Note:

- Both dividend and divisor will be 32-bit signed integers. 
- The divisor will never be 0. 
- Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. 
- For the purpose of this problem, assume that your function returns 231 − 1 
when the division result overflows.
"""


class Solution(object):
    """
    Use bit twiddling and powers of two to solve.

    Any number can be uniquely represented in binary.  for each power of two
    from 31 to zero, we check if divisor * 2^power + temp is less than the
    dividend.  If it is, xor quotient with that power of 2 and add that divisor
    * 2^power to temp.

    """

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = 0
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = temp = 0
        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                quotient |= 1 << i
                temp += divisor << i
        res = sign * quotient
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if res < MIN_INT:
            return MIN_INT
        if res > MAX_INT:
            return MAX_INT
        return res
