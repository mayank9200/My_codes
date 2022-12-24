class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        candi=0
        count=0
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        if dividend==0:
            return 0
        if divisor==1:
            return dividend
        if dividend<0:
            count+=1
            dividend=-dividend
        
        if divisor<0:
            count+=1
            divisor=-divisor  
        start=1
        end=dividend    
        while start<=end:
            mid=(start+end)//2
            if divisor*mid<=dividend:
                candi=mid
                start=mid+1
            else:
                end=mid-1
        if count==1:
            return -candi
        return candi        
        