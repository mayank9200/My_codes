class Solution:
    def solve(self,s1,s2,m,n,dp):
        if m==0 or n==0:
            return 0
        if dp[m][n]!=-1:
            return dp[m][n]
        if s1[m-1]==s2[n-1]:
            dp[m][n]=1+self.solve(s1,s2,m-1,n-1,dp)
        else:
            dp[m][n]=max(self.solve(s1,s2,m-1,n,dp),self.solve(s1,s2,m,n-1,dp))
        return dp[m][n]  
    
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m,n=len(str1),len(str2)
        dp=[[-1 for i in range(n+1)] for j in range(m+1)]
        ans=self.solve(str1,str2,m,n,dp)
        ans=''
        i=m
        j=n
        #print(dp)
        while i>=1 and j>=1: #traversing back the dp
            if str1[i-1]==str2[j-1]: #if equal then it is there
                ans=ans+str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]<dp[i][j-1]: #move towards largest
                ans=ans+str2[j-1]
                j-=1
            else:
                ans=ans+str1[i-1]
                i-=1
        while i>=1: #if str1 remains
            ans=ans+str1[i-1]
            i-=1
        while j>=1: #if str2 remains
            ans=ans+str2[j-1]
            j-=1
        return ans[::-1] 