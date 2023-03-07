#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Auxiliary Space: O(1)

        if head.next is None:
            return None

        left = head
        right = head
        for _ in range(n):
            right = right.next

        prev_left = None
        while right:
            prev_left = left
            left = left.next
            right = right.next

        if prev_left is None:
            return head.next

        if left.next is not None:
            prev_left.next = left.next
        else:
            prev_left.next = None
        return head


# @lc code=end
