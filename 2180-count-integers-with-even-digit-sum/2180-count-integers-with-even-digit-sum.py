class Solution:
    def digsum(self,i):
        summ=0
        while i>0:
            val=i%10
            summ=summ+val
            i=i//10
        return summ    
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            if self.digsum(i)%2==0:
                count+=1
        return count        
        