#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        readPointer = 0

        for _ in range(0, len(nums)):
            if nums[readPointer] == 0:
                for j in range(readPointer + 1, len(nums)):
                    nums[j - 1] = nums[j]
                nums[-1] = 0
            else:
                readPointer += 1


# @lc code=end
