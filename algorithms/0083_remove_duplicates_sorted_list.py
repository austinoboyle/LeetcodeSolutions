"""
Given a sorted linked list, delete all duplicates such that each element appear
only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Iterative Solution

    Intuition: Maintain two pointers: prev and curr.  If prev.val == curr.val,
    we can leapfrog over curr, and set prev's next pointer to curr.next.  If the
    two values are not equal, we move the prev pointer up one.
    """

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
