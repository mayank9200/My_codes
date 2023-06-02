class Solution:
    def check(self,i,target,limit):
        if limit*i>=abs(target):
            return True
        else:
            return False
        
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        val=sum(nums)
        if val==goal: #if already goal is met
            return 0
        target=goal-val
        i=1
        start=1
        end=pow(10,9)
        candi=0
        while start<=end:
            mid=(start+end)//2
            if self.check(mid,target,limit)==True:
                candi=mid
                end=mid-1
            else:
                start=mid+1
        
        return candi
    
        while True:
            if limit*i>=abs(target):
                return i
            i+=1
        return 0    
        