class Solution:
    def isvalid(self,s,i):
        return i>=0 and i<len(s)
        
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxx=0
        ans=''
        for i in range(n):
            prev=i-1
            nextt=i+1
            tans=s[i]
            while self.isvalid(s,prev) and self.isvalid(s,nextt):
                if s[prev]==s[nextt]:
                    tans=s[prev]+tans
                    tans=tans+s[nextt]
                    prev-=1
                    nextt+=1
                else:
                    break
               
            if len(tans)>maxx:
                #print(tans)
                maxx=len(tans)
                fans=tans
            if i+1<n and s[i]==s[i+1]: 
                prev=i-1
                nextt=i+2
                tans=s[i]+s[i+1]
                while self.isvalid(s,prev) and self.isvalid(s,nextt):
                    if s[prev]==s[nextt]:
                        tans=s[prev]+tans
                        tans=tans+s[nextt]
                        prev-=1
                        nextt+=1
                    else:
                        break
                if len(tans)>maxx:
                    maxx=len(tans)
                    fans=tans
        return fans
            