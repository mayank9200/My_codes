class Solution:
    def isvalid(self,s,i):
        return i>=0 and i<len(s)
    def longest_palindrome(self,s,prev,nextt,tans,fans):
        while self.isvalid(s,prev) and self.isvalid(s,nextt):
            if s[prev]==s[nextt]:
                tans=s[prev]+tans
                tans=tans+s[nextt]
                prev-=1
                nextt+=1
            else:
                break
        if len(tans)>len(fans):
            fans=tans
        return fans    

        
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxx=0
        ans=''
        fans=''
        for i in range(n):
            #odd
            tans=s[i]
            func=self.longest_palindrome(s,i-1,i+1,tans,fans)
            if len(func)>len(ans):
                ans=func
            #even
            if i+1<n and s[i]==s[i+1]:
                tans=s[i]+s[i+1]
                func=self.longest_palindrome(s,i-1,i+2,tans,fans)
                if len(func)>len(ans):
                    ans=func
        return ans        
                
            