#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp_ary = [head]
        while tmp_ary[-1].next:
            tmp_ary.append(tmp_ary[-1].next)
        return tmp_ary[len(tmp_ary) // 2]


# @lc code=end
