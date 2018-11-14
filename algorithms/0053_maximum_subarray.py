"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4] 
Output: 6 
Explanation: [4,-1,2,1] has the largest sum = 6. 

Follow up:

If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.
"""


class Solution:
    """
    Intuition:

    If all elements are negative, the maximum sum will be the greatest number in
    the array, so return it.

    The maximum contiguous subarray sum ending at any index i is equal to the
    maximum of a contiguous subarray ending at i-1 + the value at A[i]. If this
    sum is negative, set the current max sum to zero, as future subarrays would
    not want to include this value since it would only decrease their sum.

    eg
    [1, 2, 3, -3, 5, -14, 4, 8] -> max sums including i:  [1, 3, 6, 3, 8, _0_, 4, 12]

    Note setting index 5 to 0 as the maximum subarray ending there is negative,
    so we start a new subarray at index 6 and count from 0

    Example
    """

    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0
        M = max(A)
        if M < 0:
            return M
        curr = 0
        for i in A:
            curr += i
            if curr < 0:
                curr = 0
            M = max(M, curr)
        return M
