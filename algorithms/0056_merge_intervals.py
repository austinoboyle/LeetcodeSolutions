# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    """
    Intuition:

    If we sort the starts and ends together in one array, we can keep track of
    how many intervals are currently open.  NOTE: Ends should be sorted
    after starts because if one interval starts where another ends, we don't
    want to treat that as two separate intervals.

    EG [[1, 2], [2, 4]] Becomes [(1, START), (2, START), (2, END), (4, END)]

    As we loop through this combined array, we keep track of the number of open
    intervals.  We add/subtract 1 from the number of open intervals if we
    encounter a START/END respectively.

    If none are open, and we encounter a START, set the start of a new interval 
    to the current val.  If 1 is open and we encounter an END, add new interval
    (start, curr_val) to the merged interval list.
    """

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        START = 0
        END = 1
        if len(intervals) < 2:
            return intervals
        starts = [(i.start, START) for i in intervals]
        ends = [(i.end, END) for i in intervals]
        merged = []
        L = sorted(starts + ends)
        numActive = 0
        start = L[0][0]
        for el in L:
            if el[1] == START:
                if numActive == 0:
                    start = el[0]
                numActive += 1
            else:
                numActive -= 1
                if numActive == 0:
                    merged.append(Interval(start, el[0]))
        return merged
