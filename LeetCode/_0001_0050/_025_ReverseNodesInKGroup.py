#-----------------------------------------------------------------------------
# Runtime: 48ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import sys
sys.path.append('LeetCode')

from ListNode import ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head
        p1, p2, p3 = dummy_head, head, head
        while p2 is not None and p3 is not None:
            for _ in range(k):
                if p3 is None:
                    return dummy_head.next
                p3 = p3.next

            for _ in range(k):
                temp_next = p2.next
                p2.next = p3
                p3 = p2
                p2 = temp_next
            p1.next = p3

            for _ in range(k):
                p1 = p1.next
            p2 = p1.next
            p3 = p1.next

        return dummy_head.next
