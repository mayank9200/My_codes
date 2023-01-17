class Solution:
    def countDigits(self, num: int) -> int:
        val=num
        count=0
        while num>0:
            temp=num%10
            if val%temp==0:
                count+=1
            num=num//10
        return count    
            
        