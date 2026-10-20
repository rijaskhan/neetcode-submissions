class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dctA={}
        dctB={}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if (c1 in dctA and dctA[c1] !=c2) or (c2 in dctB and dctB[c2] !=c1):
                return False
            dctA[c1]=c2
            dctB[c2]=c1
        return True


        