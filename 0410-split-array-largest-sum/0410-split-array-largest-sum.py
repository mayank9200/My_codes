class Solution:
     def ispossible(self,nums,mid,k):
        d=1
        summ=0
        for i in nums:
            summ=summ+i
            if summ>mid:
                d+=1
                summ=i
        return d  
     def splitArray(self, nums: List[int], k: int) -> int:
        start=max(nums)
        end=sum(nums)
        candi=max(nums)
        while start<=end:
            mid=(start+end)//2
            if self.ispossible(nums,mid,k)==k:
                candi=mid
                end=mid-1
            elif self.ispossible(nums,mid,k)<k:
                candi=mid
                end=mid-1
            else:
                start=mid+1
        return candi   
        