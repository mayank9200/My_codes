class Solution:
    def solve(self,s1,s2,m,n,dp):
        if m==0:
            return n
        if n==0:
            return m
        if dp[m][n]!=-1:
            return dp[m][n]
        if s1[m-1]==s2[n-1]:
            dp[m][n]=self.solve(s1,s2,m-1,n-1,dp)
        else:
            dp[m][n]=min(1+self.solve(s1,s2,m-1,n,dp),1+self.solve(s1,s2,m,n-1,dp),1+self.solve(s1,s2,m-1,n-1,dp))
        return dp[m][n]  
    
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[-1 for i in range(n+1)] for j in range(m+1)]
        ans=self.solve(word1,word2,m,n,dp)
        return ans