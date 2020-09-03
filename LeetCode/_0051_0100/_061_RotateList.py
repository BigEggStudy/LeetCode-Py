#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import sys
sys.path.append('LeetCode')

from ListNode import ListNode

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head is None: return head

        pointer = ListNode(-1)
        pointer.next = head
        length = 0
        while pointer.next is not None:
            pointer = pointer.next
            length += 1
        pointer.next = head

        k = length - (k % length)
        while k > 0:
            pointer = pointer.next
            k -= 1

        head = pointer.next
        pointer.next = None
        return head
