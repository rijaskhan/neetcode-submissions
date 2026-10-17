class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        freq=[[]for i in range(len(nums)+1)]
        result=[]
        for x in nums:
            if x in dct:
                dct[x]+=1
            else:
                dct[x]=1
        for item,count in dct.items():
            freq[count].append(item)
        for x in range(len(freq)-1,0,-1):
            for num in freq[x]:
                result.append(num)
                if len(result)==k:
                    return result
            

            



        