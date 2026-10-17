class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest=0
        # for i in range(len(s)):
        #     seen =set()
        #     for j in range(i,len(s)):
        #         if s[j] not in seen:
        #             seen.add(s[j])
        #         else:
        #             break
        #     longest=max(longest,len(seen))
        # return longest
        longest=0
        l=0
        seen=set()
        for r in range(len(s)):
            while s[r]in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest=max(longest,len(seen))
        return longest
        