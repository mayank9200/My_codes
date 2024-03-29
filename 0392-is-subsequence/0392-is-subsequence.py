class Solution:
    # def solve(self,s1,s2,m,n,dp):
    #     if m==0 or n==0:
    #         return 0
    #     if dp[m][n]!=-1:
    #         return dp[m][n]
    #     if s1[m-1]==s2[n-1]:
    #         dp[m][n]=1+self.solve(s1,s2,m-1,n-1,dp)
    #     else:
    #         dp[m][n]=max(self.solve(s1,s2,m-1,n,dp),self.solve(s1,s2,m,n-1,dp))
    #     return dp[m][n]    
    def isSubsequence(self, s: str, t: str) -> bool:
        # m,n=len(s),len(t)
        # dp=[[-1 for i in range(n+1)] for j in range(m+1)]
        # return len(s)==self.solve(s,t,m,n,dp) #if lcs is s and t is s
        #another way then lcs, two pointer approach
        i=0
        j=0
        m,n=len(s),len(t)
        count=0
        while i<m and j<n:
            if s[i]==t[j]: #if same then increase both
                count+=1
                i+=1
                j+=1
            else:
                j+=1 #if not increase only j
        return count==len(s)        
        
        