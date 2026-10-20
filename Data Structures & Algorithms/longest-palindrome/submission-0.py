class Solution:
    def longestPalindrome(self, s: str) -> int:
        dct={}
        res=0
        # dct=defaultdict(int)
        for char in s:
            dct[char]=0
        for char in s:
            dct[char]+=1
            if dct[char]%2==0:
                res+=2
        for x in dct.values():
            if x%2==1:
                res+=1
                break
        return res


        