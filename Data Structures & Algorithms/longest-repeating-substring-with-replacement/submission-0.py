class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        dct={}
        longest=0
        for i in range(len(s)):
            ch=s[i]
            if ch in dct:
                dct[ch]+=1
            else:
                dct[ch]=1
            max_freq=max(dct.values())
            while (i-l+1)-max_freq>k:
                dct[s[l]]-=1
                l+=1
                max_freq=max(dct.values())
            longest=max(longest,i-l+1)
        return longest





        