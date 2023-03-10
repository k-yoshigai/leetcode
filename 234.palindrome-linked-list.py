#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # Find the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Check whether the list is palindrome or not
        left = head
        right = prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


# @lc code=end
