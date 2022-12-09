class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ=0
        prod=1
        while n>0:
            temp=n%10
            summ+=temp
            prod*=temp
            n=n//10
        return prod-summ    
        