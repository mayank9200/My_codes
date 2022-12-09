class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        count=0
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]>1:
                count+=d[i]*(d[i]-1)//2
        return count        
        