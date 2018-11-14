"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


class Solution:
    """
    Algorithm:

    Keep track of a few vars:
        - ui: where we WOULD be if we were in the UPDATED array at this point
        - duplicate_count: number of consecutive duplicates
        - deletes: list of deletions to make of form [(start_index, num)]
        - curr: most recent element looked at

    1. For every element in A, if it is the same as most recent el, increment
       duplicate_count.  Otherwise, if duplicate_count is greater than
       MAX_OCCURENCES, add a deletion from the current ui with a duplicate_count
       of the difference between duplicate_count and max occurences. Set 
       duplicate_count to 1 and curr to el.
    2. If our duplicate count is not greater than MAX_OCCURENCES, increment ui
    3. Go through list of deletions and delete deletion.count elements from the 
        array starting at deletion.start.  Keep track of number of elements
        deleted. 
    4. Return N - total number of deletions

    Intuition is as such.  We want to delete all consecutive duplicate groups of
    length > MAX_OCCURENCES.  In this case, MAX_OCCURENCES = 1, but this
    solution extends to other values as well.  So, we keep track of spots to
    start deleting, and how many elements to delete starting at that spot.

    """

    def removeDuplicates(self, A, MAX_OCCURENCES=1):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0
        ui = 0
        duplicate_count = 1
        N = len(A)
        deletes = []
        curr = A[0]
        for el in A[1:]:
            if el != curr:
                if duplicate_count > MAX_OCCURENCES:
                    deletes.append((ui, duplicate_count - MAX_OCCURENCES))
                duplicate_count = 1
                curr = el
            else:
                duplicate_count += 1
            if duplicate_count <= MAX_OCCURENCES:
                ui += 1

        if duplicate_count > MAX_OCCURENCES:
            deletes.append((ui, duplicate_count - MAX_OCCURENCES))
        totalRemoved = 0
        for start, count in deletes:
            del A[start: start+count]
            totalRemoved += count
        return N - totalRemoved
