class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        arr=[]
        curr=1
        prev=0
        ans=0
        n=len(s)
        for i in range(1,n):
            if s[i]==s[i-1]:
                curr+=1
            else:
                ans=ans+min(curr,prev)
                prev=curr
                curr=1      
        return ans+min(curr,prev)
            
                
        