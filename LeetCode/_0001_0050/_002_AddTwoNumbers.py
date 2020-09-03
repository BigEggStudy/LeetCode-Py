#-----------------------------------------------------------------------------
# Runtime: 112ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import sys
sys.path.append('LeetCode')

from ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(-1)
        current = result
        carry = 0

        while l1 or l2 or carry:
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            sum += carry

            carry = 0
            if sum >= 10:
                sum -= 10
                carry = 1
            current.next = ListNode(sum)
            current = current.next

        return result.next
