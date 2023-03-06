#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Time complexity: O(m+n)
        # Auxiliary Space: O(1)

        if headA is None or headB is None:
            return None

        ptr1, ptr2 = headA, headB

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            if ptr1 == ptr2:
                return ptr1

            if ptr1 is None:
                ptr1 = headB

            if ptr2 is None:
                ptr2 = headA

        return ptr1


# @lc code=end
