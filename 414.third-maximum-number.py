#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#


# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        different_count = 0
        prev_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != prev_num:
                different_count += 1
                prev_num = nums[i]
            if different_count == 2:
                return nums[i]
        return nums[0]


# @lc code=end
