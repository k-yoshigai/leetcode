#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def intersection(self, head) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        intersection = self.intersection(head)
        if intersection is None:
            return None

        start = head
        while start != intersection:
            start = start.next
            intersection = intersection.next
        return start


# @lc code=end
