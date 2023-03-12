#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        head1 = list1
        head2 = list2

        node1 = list1
        node1_prev = None
        node2 = list2
        node2_prev = None

        start_node = 0

        while node1 and node2:
            if node1 and node1.val <= node2.val:
                if start_node == 0:
                    start_node = 1
                while node1 and node1.val <= node2.val:
                    node1_prev = node1
                    node1 = node1.next
                node1_prev.next = node2
            elif node2 and node2.val < node1.val:
                if start_node == 0:
                    start_node = 2
                while node2 and node2.val < node1.val:
                    node2_prev = node2
                    node2 = node2.next
                node2_prev.next = node1

        return head1 if start_node == 1 else head2


# @lc code=end
