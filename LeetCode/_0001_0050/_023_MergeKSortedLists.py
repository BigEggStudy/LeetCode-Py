#-----------------------------------------------------------------------------
# Runtime: 64ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import sys
sys.path.append('LeetCode')

from ListNode import ListNode

import heapq

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        dummy_head = current = ListNode(-1)
        heap = [(list_head.val, i, list_head) for i, list_head in enumerate(lists) if list_head]
        heapq.heapify(heap)

        while len(heap) > 0:
            _, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy_head.next
