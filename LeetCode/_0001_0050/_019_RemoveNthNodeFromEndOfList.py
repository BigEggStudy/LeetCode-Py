#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import sys
sys.path.append('LeetCode')

from ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None or n < 0:
            return None

        dummy_head = ListNode(-1)
        dummy_head.next = head

        node1 = dummy_head
        node2 = dummy_head

        for i in range(n):
            node1 = node1.next
            if node1 is None:
                return None

        while node1.next is not None:
            node1 = node1.next
            node2 = node2.next
        node2.next = node2.next.next

        return dummy_head.next
