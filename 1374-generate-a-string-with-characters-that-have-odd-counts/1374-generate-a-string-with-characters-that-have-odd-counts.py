class Solution:
    def generateTheString(self, n: int) -> str:
        if n==1:
            return 'a'
        if n%2==0:
            val=n//2
            if val%2==0:
                ans='a'*(val+1)+'b'*(val-1)
            else:
                ans='a'*val+'b'*val
        else:
            val=n//2
            if val%2==0:
                ans='a'*(val+1)+'b'*(val-1)
            else:
                ans='a'*val+'b'*val
            ans=ans+'c'    
        return ans   
        