class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        c=0
        if n==1 or n==2:
            return n
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
        return c    
        