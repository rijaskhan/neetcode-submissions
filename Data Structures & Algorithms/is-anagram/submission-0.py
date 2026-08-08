class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct={}
        if len(s)!=len(t):
            return False
        for x in s:
            if x in dct:
                dct[x]+=1
            else:
                dct[x]=1
        for x in t:
            if x in dct:
                dct[x]-=1
                if dct[x]==0:
                    del dct[x]
            else:
                return False
        return True
        