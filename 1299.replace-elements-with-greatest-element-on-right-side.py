#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#


# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < max_num:
                arr[i] = max_num
            elif arr[i] > max_num:
                max_num, arr[i] = arr[i], max_num
        return arr


# @lc code=end
