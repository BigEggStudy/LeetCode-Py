import sys, queue
sys.path.append('LeetCode')

from ListNode import ListNode
from TreeNode import TreeNode

def generateLinkList(nums: []) -> ListNode:
    if nums is None or len(nums) == 0:
        return None

    head = ListNode(-1)
    current = head

    for num in nums:
        current.next = ListNode(num)
        current = current.next

    return head.next

def generateTree(nums: []) -> TreeNode:
    if nums is None or len(nums) == 0:
        return None

    index = 0
    root = TreeNode(nums[index])
    index += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current = q.get()
        if index < len(nums) and nums[index] is not None:
            node = TreeNode(nums[index])
            current.left = node
            q.put(node)
        if index + 1 < len(nums) and nums[index + 1] is not None:
            node = TreeNode(nums[index + 1])
            current.right = node
            q.put(node)
        index += 2

    return root
