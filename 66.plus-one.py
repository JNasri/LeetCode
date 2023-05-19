#
#
# My Solution with no help
# 
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        # empty string to store numbers
        string = ""
        # list to add numbers after +1
        array = []

        # while list still exist
        while digits:
            # add the number to the string
            string = string + str(digits.pop(0))

        # convert string to int , +1 , reconvert to string    
        string = int(string)
        string += 1
        string = str(string)

        # iterater over the string and add numbers to array 
        for i in string:
            array.append(int(i))
        
        # return array
        return array



#
#
# Leetcode solution
#
#
class Solution(object):
    def plusOne(self, digits):
        digits=[str(i) for i in digits]
        s=''.join(digits)
        a=int(s)+1
        l=list(str(a))
        l=[int(i) for i in l]
        return l

# pretty much the same approach, which is:
# - Convert each list element to string
# - Convert to int then add 1 then back to string
# - Iteracte over string to add to the new list and return it


    
