#
# My solution with no help (same as LeetCode Solution)
#
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # start from end of string
        i = -1
        # counter of num of characters
        counter = 0

        # while there are spaces at the end of the string
        while s[i].isspace():
            # move left
            i = i - 1
        
        # while there is a letter in the char count and return counter
        try:
            while not s[i].isspace():
                # increase counter
                counter+=1
                i -= 1
            return counter
        # if out of range (end of string) return counter
        except:
            return counter
        


#
#
# LeetCode Solution 
#
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        i = len(s)-1
        while s[i] != " " and i>=0:
            i-=1

        return (len(s)-1)-i


# This is a better solution that mine, and it uses the rstripe to remove
# all spaces from the right (only last word appears from s[-1])
# then we can calculate how long it is.
# NOTE: my solution uses isspace() and a counter. More clearer than the LeetCode one

