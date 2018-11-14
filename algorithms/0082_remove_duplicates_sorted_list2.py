"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5 Output: 1->2->5 

Example 2:

Input: 1->1->1->2->3 Output: 2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Recursive Solution.  
    BASE CASE:
        head or head.next is None, return head.

    -  If the head's val is equal to the next val, move head 
       to the first non-duplicate value, and return the recursive call on the
       new head.
    -  Otherwise, we keep head where it is, and set head's next pointer to the
       recursive call on head.next, and then return head
    """

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            val = head.val
            while head and head.val == val:
                head = head.next
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
