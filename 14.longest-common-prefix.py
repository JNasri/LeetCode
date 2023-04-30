#
# My solution with some help from the internet
#
#
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # a string to hold the first list item
        longestPrefix = strs[0]

        # for loop : iterate through strings starting from index 1
        for i in range(1, len(strs)):
            # while loop : compare characters while longestPrefix still exists
            while(longestPrefix != ""):
                # try so that if an index is out of bound, we do the except part
                try:
                    # if sting[i] and longestPrefix match character
                    if str.index(str(strs[i]),longestPrefix) == 0:
                        # break the loop iteration 
                        break
                    else:
                        # remove the fisrt character since it doesn't match
                        longestPrefix = longestPrefix[:-1]
                except:
                    # index is out of bound, remove first character
                    longestPrefix = longestPrefix[:-1]

        # reutrn the string
        return longestPrefix


#
# LeetCode Answer
#
class Solution:
    def longestCommonPrefix(self, v: list[str]) -> str:
        # empty string to store the longestPrefix, not like I did
        ans="" 
        # sort the list so we can find the answer faster
        v=sorted(v)
        print(v)
        first=v[0]
        last=v[-1]
        # Iterate characters of first & last string in list, stopping at length of shorter one
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

## This answer is very impressive, let's say we have :
# List = ["Approach" , "Appear" , "Apple" , "Apartment"]
# sort them, we get ["Apartment" , "Appear" , "Apple" , "Approach"]
# first is "Apartment" , last is  "Approach"
# the loop will iterate with min length "Approach"
# test if they match or not, and return the answer.. that's it.