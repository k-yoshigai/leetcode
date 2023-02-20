#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = m - 1, n - 1, m + n - 1
        while k >= 0:
            if i >= 0 and j >= 0:
                if nums2[j] >= nums1[i]:
                    nums1[k] = nums2[j]
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                j -= 1
            else:
                break
            k -= 1


# @lc code=end
