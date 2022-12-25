class Solution:
    #https://youtu.be/QYwWrVIFAwE
    def check(self,n):
        x=5
        count=0
        while x<=n:
            count=count+n//x
            x=x*5
        return count    
            
    def preimageSizeFZF(self, k: int) -> int:
        start=0
        end=pow(10,10)
        while start<=end:
            mid=(start+end)//2
            num_zeros=self.check(mid)
            if num_zeros==k:
                return 5
            elif num_zeros>k:
                end=mid-1
            else:
                start=mid+1
        return 0        
        
        