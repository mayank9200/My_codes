class Solution:
    def ispossible(self,mid,piles,h):
        count=0
        for i in piles:
            count=count+i//mid
            tval=i%mid
            if tval>0:
                count+=1
        return count<=h     
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)+1
        while start<end:
            mid=(start+end)//2
            if self.ispossible(mid,piles,h):
                candi=mid
                end=mid
            else:
                start=mid+1
        return candi        
        