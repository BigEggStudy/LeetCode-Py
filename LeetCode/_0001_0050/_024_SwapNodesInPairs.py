#-----------------------------------------------------------------------------
# Runtime: 28ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import sys
sys.path.append('LeetCode')

from ListNode import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        dummy_head = ListNode(-1)
        dummy_head.next = head
        p1, p2, p3 = dummy_head, head, head.next

        while p2 is not None and p3 is not None:
            p2.next = p3.next
            p3.next = p2
            p1.next = p3

            p1 = p2
            p2 = p2.next
            if p2 is None:
                break
            p3 = p2.next

        return dummy_head.next
