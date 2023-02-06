class Solution:
    def ispossible(self,mid,piles,h):
        count=0
        for i in piles:
            count=count+i//mid # kitne hours to eat that particular piles a 'mid' speed 
            tval=i%mid #if something is remaining then add one
            if tval>0:  #basically take ceil value in case of decimal
                count+=1
        return count<=h     # was the time taken less than s
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)+1
        while start<end:
            mid=(start+end)//2
            if self.ispossible(mid,piles,h): #do we have a ans
                candi=mid #candidate
                end=mid # search for any better ans
            else:
                start=mid+1
        return candi        
        