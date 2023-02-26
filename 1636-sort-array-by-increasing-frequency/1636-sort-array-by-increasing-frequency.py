class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        h=[]
        for i in d:
            heappush(h,[d[i],-i])
        i=0
        while len(h)>0:
            freq,val=heappop(h)
            for j in range(freq):
                nums[i]=-val
                i+=1
        return nums      
            
        