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
    def minInsertions(self, s: str) -> int:
        m,n=len(s),len(s)
        s2=s[::-1]
        dp=[[-1 for i in range(n+1)] for j in range(m+1)]
        return len(s)-self.solve(s,s2,m,n,dp) #min insertions = min deletions
        