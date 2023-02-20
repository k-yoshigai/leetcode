#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex


# @lc code=end
