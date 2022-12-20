class Solution:
    def ispossible(self,weights,mid,days):
        d=1
        summ=0
        for i in weights:
            summ=summ+i
            if summ>mid:
                d+=1
                summ=i
        return d        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start=max(weights)
        end=sum(weights)
        candi=max(weights)
        while start<=end:
            mid=(start+end)//2
            if self.ispossible(weights,mid,days)==days:
                candi=mid
                end=mid-1
            elif self.ispossible(weights,mid,days)<days:
                candi=mid
                end=mid-1
            else:
                start=mid+1
        return candi        
            