#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#


# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 1:
            return False

        passed_top = False
        started = False
        for i in range(1, len(arr)):
            if not started and arr[i] > arr[i - 1]:
                started = True
            elif started and not passed_top and arr[i] < arr[i - 1]:
                passed_top = True
            elif arr[i] == arr[i - 1] or passed_top and arr[i] > arr[i - 1] or not passed_top and arr[i] < arr[i - 1]:
                return False

        if started and passed_top:
            return True
        return False


# @lc code=end
