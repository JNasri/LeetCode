#
# This problem was difficult, here's the leetcode solution 
#
#
class Solution:
    def mySqrt(self, x: int) -> int:
        # if input is 0 return 0
        if x == 0:
            return 0
        # iterate over number from 1 to x+1
        for i in range(1,x+1):
            if i * i == x:
                return i
            # if we exceed the input value, return the last i (round to smallest)
            elif i * i > x:
                return (i-1)

        return num

        