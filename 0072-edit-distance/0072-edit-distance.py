class Solution:
    def solve(self,s1,s2,m,n,dp):
        #it is very important to note that what is to be returned, as per the return type of the function(count,min/max,sum etc)
        if m==0:
            return n #require n moves
        if n==0:
            return m #require m moves
        if dp[m][n]!=-1:
            return dp[m][n]
        if s1[m-1]==s2[n-1]:
            dp[m][n]=self.solve(s1,s2,m-1,n-1,dp) #if both are same then find in remianing
        else:
            dp[m][n]=min(1+self.solve(s1,s2,m-1,n,dp),1+self.solve(s1,s2,m,n-1,dp),1+self.solve(s1,s2,m-1,n-1,dp)) #min of deletion,insertion and replacement, adding 1 because 1 move have been made
        return dp[m][n]  
    
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[-1 for i in range(n+1)] for j in range(m+1)]
        ans=self.solve(word1,word2,m,n,dp)
        return ans