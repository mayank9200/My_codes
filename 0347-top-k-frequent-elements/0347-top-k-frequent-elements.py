class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappush,heappop
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        h=[] 
        ans=[]
        print(d)
        for i in d:
            heappush(h,[d[i],i])
            if len(h)>k:
                temp,val=heappop(h)
        while len(h)>0:
            ans.append(heappop(h)[1])
        return ans    
        