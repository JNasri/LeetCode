#
#
# The internet solution (NOT MINE LOL)
#
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # I got this line from the internet 
        #
        # basically, make the strings int and base 2 (binary)
        # then add them together (binary addition)
        # then format the answer as a string
        # then return it
        return '{0:b}'.format(int(a, 2) + int(b, 2))
   

