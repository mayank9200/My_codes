class Solution:
    def numberOfMatches(self, n: int) -> int:
        count=0
        while n>0:
            if n%2==0:
                count=count+n//2         
            else:
                count=count+n//2+1
            n=n//2
            #print(n)
        return count-1
        