#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#


# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr) - 1:
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[i] == arr[j] / 2:
                    return True
            i += 1
        return False


# @lc code=end
