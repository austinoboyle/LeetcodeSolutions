"""
Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start
times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5] Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]] Explanation: Because the new interval [4,8]
overlaps with [3,5],[6,7],[8,10].
"""


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    """
    Intuition:
    Find where the start and end of the new interval would fit in with the
    existing intervals. We want elements left of the start of the new interval,
    elements right of the end of the interval, and everything it overlaps.

    We return left + [newI] + right

    If newI.start or newI.end land in an existing interval, we extend the
    boundaries of newI to the edge of that interval.

    return intervals to the left of start + newI + intervals right of end
    """

    def insert(self, A, newI):
        N = len(A)
        leftEnd = 0
        rightStart = len(A) - 1
        while leftEnd <= rightStart and newI.start > A[leftEnd].end:
            leftEnd += 1
        while rightStart >= 0 and newI.end < A[rightStart].start:
            rightStart -= 1

        # Handle start/end in the middle of an existing interval.  Extend newI
        # to the edges of those intervals.
        if leftEnd < N and A[leftEnd].start <= newI.start:
            newI.start = A[leftEnd].start
        if rightStart >= 0 and A[rightStart].end >= newI.end:
            newI.end = A[rightStart].end
        return A[:leftEnd] + [newI] + A[rightStart + 1:]
