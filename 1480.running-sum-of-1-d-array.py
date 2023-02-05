#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        tmp_sum = 0
        for i in range(len(nums)):
            current_num = nums[i]
            nums[i] += tmp_sum
            tmp_sum += current_num

        return nums


# @lc code=end
