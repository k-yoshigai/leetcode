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
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True


# @lc code=end
