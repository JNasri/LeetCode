#
# My solution with no help
#
#
class Solution:
    def romanToInt(self, s: str) -> int:
        # check if input is not correct
        if(len(s) < 1 or len(s) > 15):
            return "Input is Invalid"

        # make all letters uppercase
        s = s.upper()
        
        # check if string contains only roman
        roman = "IVXLCDM"
        for i in range(len(s)):
            if s[i] not in roman:
                return "Input is Invalid"
        
        # variable to hold the sum
        x = 0

        # define the irregular cases
        if(s.find("IV") > -1):
            x += 4
            s = s.replace("IV", "")
        if(s.find("IX") > -1):
            x += 9
            s = s.replace("IX", "")
        if(s.find("XL") > -1):
            x += 40
            s = s.replace("XL", "")
        if(s.find("XC") > -1):
            x += 90
            s = s.replace("XC", "")
        if(s.find("CD") > -1):
            x += 400
            s = s.replace("CD", "")
        if(s.find("CM") > -1):
            x += 900
            s = s.replace("CM", "")

        # iterate over the string and add
        for i in range(len(s)):
            if(s[i] == "I"):
                x += 1
            if(s[i] == "V"):
                x += 5
            if(s[i] == "X"):
                x += 10
            if(s[i] == "L"):
                x += 50
            if(s[i] == "C"):
                x += 100
            if(s[i] == "D"):
                x += 500
            if(s[i] == "M"):
                x += 1000
        
        return x;      


#
# LeetCode Answer
#
class Solution:
    def romanToInt(self, s: str) -> int:

        total = 0
        #creating a dict is better than the if statements I did
        theDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        # add all integers (even the irregular ones)
        for i in s:
            total += theDict[i]

        # now, we remove the amount necessery to make the sum right
        # this is smart I admit my stupidity :/

        # Example: IV will be added as 6 and we want 4, so just subtract 2!
        if "IV" in s:
            total -= 2
        # 11 will be added and we need it to be 9 , so just subtract 2... and so on
        if "IX" in s:
            total -= 2
        if "XL" in s:
            total -= 20
        if "XC" in s:
            total -= 20
        if "CD" in s:
            total -= 200
        if "CM" in s:
            total -= 200


        return total
