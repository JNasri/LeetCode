#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # pointer for last item in nums1
        c1 = m-1
        # pointer for last item in nums2
        c2 = n-1
        # pointer for last item in the nums1 including zeros
        k = m + n - 1

        # while nums2 is not empty
        while c2 >= 0:
            # if nums1 still has numbers and number its current number is larger
            if c1 >= 0 and nums1[c1] > nums2[c2]:
                # add the large number to last of the nums1
                nums1[k] = nums1[c1];
                # move the pointer to the left in nums1
                c1 -= 1
            # if nums2 number is larger than nums1
            else:
                # add the large number to the last of the nums1
                nums1[k] = nums2[c2];
                # move pointer to the left in nums2
                c2 -= 1
            # shift the pointer of all nums1 (including zeros) to left
            k -= 1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
# @lc code=end

