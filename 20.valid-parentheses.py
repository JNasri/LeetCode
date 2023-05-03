#
# My solution with some help from the internet
#
#
class Solution:
    def isValid(self, s: str) -> bool:

        # initialize parentheses dict
        Dict = {'(':')','{':'}','[':']'}
        stack = []
        # if string is not even length (2,4,6..), no need to check anything
        if len(s) % 2 != 0:
            return False

        for char in s:
            # push opening bracket to stack
            if char in Dict.keys():
                stack.append(char)
            else:
                # closing bracket without matching opening bracket
                if stack == []:
                    # no open bracket to match the closed, so return false
                    return False
                # if closing bracket -> pop stack top
                open_brac = stack.pop()
            # not matching bracket -> invalid!
                if char != Dict[open_brac]:
                    return False
                                   
        return stack == []



#
# LeetCode Answer
#

# The answer is very similar to my answer, in fact, all websites solved this
# probelm with the same kind of logic : a stack to hold parentheses and a dict
# to hold the pairs of parentheses.

