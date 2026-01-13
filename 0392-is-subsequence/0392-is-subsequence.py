class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexS = 0
        indexT = 0
        for indexT in range(len(t)):
            if indexS < len(s) and t[indexT] == s[indexS]:
                indexS+=1
        if indexS == len(s):
            return True
        else: 
            return False


        