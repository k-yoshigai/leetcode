#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def print(self, head: ListNode) -> None:
        node = head
        print("[", end="")
        while node:
            print(node.val, end=",")
            node = node.next
        print("]")

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        if head is None:
            return None

        odd = head
        even = head.next
        even_head = even

        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


# @lc code=end
