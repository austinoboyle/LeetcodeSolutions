"""
Two Solutions:

1. Recursive
    Use helper function that takes two list heads and a carry digit.
    BASE CASE:
        - Both Lists are None -> Return None
    i. Get the sum of the digits (+ carry) in that position (None = 0)
    ii. Create new Node with value sum % 10
    iii. RECURSIVE CALL: Make new Node's next node the return value of calling
    addHelper on l1.next, l2.next, and sum // 10.
    iv. return the new Node

2. Iterative
    Similar approach, without recursive calls.  Set two pointers to be the
    current digit of each list.  Move along both lists, creating a new list with
    the sum of the values in each respective list (None = 0) + a carry that is
    calculated at each digit sum.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addRecursive(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type carry: int
        :rtype: ListNode
        """
        if not l1 and not l2 and not carry:
            return None
        s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry, dig = divmod(s, 10)
        newL = ListNode(dig)
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        newL.next = self.addRecursive(next1, next2, carry)
        return newL

    def addIterative(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = None
        curr1, curr2 = l1, l2
        while curr1 or curr2 or carry:
            s = carry + (curr1.val if curr1 else 0) + \
                (curr2.val if curr2 else 0)
            carry, dig = divmod(s, 10)
            newNode = ListNode(dig)
            if not head:
                head = newNode
                ptr = head
            else:
                ptr.next = newNode
                ptr = ptr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return head
