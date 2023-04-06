class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n!=1:
            if n in s:
                return False
            s.add(n)
            nn=0
            while n>0:
                temp=n%10
                nn=nn+temp*temp
                n=n//10
            n=nn
        return True    
                
        