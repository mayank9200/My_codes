class Solution:
    def numTrees(self, n: int) -> int:
        #simple catalan number ques
        #C0=c0, C1=c0c1+c1c0 , C2=c0c2+c1c1+c2c0, C3=c0c3+c1c2+c2c1+c3c0......
        #https://www.youtube.com/watch?v=H1qjjkm3P3c&list=PL-Jc9J83PIiEZvXCn-c5UIBvfT8dA-8EG&index=16
        if n==0 or n==1:
            return 1
        dp=[0 for i in range(n+1)]
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]=dp[i]+dp[j]*dp[i-j-1]
        return dp[n]      
        