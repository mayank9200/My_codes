class Solution:
    def isPalindrome(self, x: int) -> bool:
        nn=0
        
        if x<0:
            return False
        xx=x
        while x>0:
            temp=x%10
            nn=nn*10+temp
            x=x//10
        print(nn)    
        return nn==xx
        