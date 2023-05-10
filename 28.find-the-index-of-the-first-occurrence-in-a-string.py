#
# My solution with no help (same as LeetCode Solution)
#
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
# haystack = "sadbutsad"
# needle = "sad"
# print(Solution().strStr(haystack, needle))

