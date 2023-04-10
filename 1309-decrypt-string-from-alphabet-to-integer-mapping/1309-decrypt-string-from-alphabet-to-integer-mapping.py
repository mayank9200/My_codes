class Solution:
    def freqAlphabets(self, s: str) -> str:
        d={}
        for i in range(1,10):
            d[str(i)]=chr(ord('a')+(i-1))
        for i in range(10,27):
            d[str(i)+'#']=chr(ord('j')+(i-10))
        n=len(s)
        i=0
        ans=''
        while i<n:
            if i+2<n and s[i+2]=='#':
                ans=ans+d[s[i:i+3]]
                i=i+3
            else:
                ans=ans+d[s[i]]
                i=i+1
        return ans        
        