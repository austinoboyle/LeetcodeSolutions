"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution(object):
    """
    Intuition: first missing positive in an array of length N must be in range
    [1, N+1] inclusive.  We want to take advantage of this by storing counts of
    each element [1,N] in the array itself.  

    Do a first pass to get rid of values we don't care about (< 0 or > N).  We
    also multiply each number by N to keep track of the ORIGINAL value of the
    array at the position.

    Do a second pass, get the original value at a spot.  If original is not 0
    and A[original - 1] has not been incremented it yet, increment by 1

    Do a third pass, checking if A[i] % N == 0, if it is, return i + 1

    If we get through the array, all elements [1,N] were stored in original
    array, so return N+1
    """

    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(A)
        if N <= 1:
            return 1 if not A or A[0] != 1 else 2

        for i in range(N):
            if A[i] < 0 or A[i] > N:
                A[i] = 0
            A[i] *= N

        for el in A:
            if el // N > 0 and A[el//N - 1] % N == 0:
                A[el//N - 1] += 1
        for i in range(N):
            if A[i] % N == 0:
                return i + 1
        return N + 1
