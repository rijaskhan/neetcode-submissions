class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # sol1
        # ans=nums*2
        # return ans
        
        # sol2
        ans=[0]*(2*len(nums))
        for i in range(len(nums)):
            ans[i]=nums[i]
            ans[i+len(nums)]=nums[i]
        return ans