class Solution:
    def numDecodings(self, s: str) -> int:
        #https://www.youtube.com/watch?v=jFZmBQ569So
        #make 4 cases , last two are (0,0),(0,non 0),(non 0,0),(non 0,non 0)
        n=len(s)
        dp=[0 for i in range(n)]
        if s[0]=='0':
            dp[0]=0
        else:
            dp[0]=1
        
        #make cases and see
        for i in range(1,n):
            if s[i]!='0' and s[i-1]!='0':
                if int(s[i-1:i+1])<=26: #if value is less than 26
                    dp[i]=dp[i-1]+(dp[i-2] if i-2>=0 else 1)
                else:
                    dp[i]=dp[i-1]
            elif s[i]!='0' and s[i-1]=='0':
                dp[i]=dp[i-1]
            elif s[i]=='0' and s[i-1]!='0':
                if int(s[i-1:i+1])<=26:
                    dp[i]=(dp[i-2] if i-2>=0 else 1)
                else:
                    dp[i]=0
            elif s[i]=='0' and s[i-1]=='0':    
                dp[i]=0
        #print(dp)
        return dp[n-1]    
                
        