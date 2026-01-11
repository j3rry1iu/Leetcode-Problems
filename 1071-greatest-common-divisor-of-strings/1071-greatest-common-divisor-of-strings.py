class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        len1 = len(str1)
        len2 = len(str2)
        length = min(len1, len2)
        while length > 0: 
            if len2 % length == 0 and len1 % length == 0:
                firstDivide = int(len1 / length)
                secondDivide = int(len2 / length)
                if str1[:length] * firstDivide == str1 and str1[:length] * secondDivide == str2: 
                    return str1[:length]
                else: 
                    length -= 1
            else: 
                length -= 1  
        return ""



        