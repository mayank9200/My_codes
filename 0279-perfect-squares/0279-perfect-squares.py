class Solution:
    def unboundknapsack(self,arr,n,summ,dp):
        if n==0:
            return float('inf')
        if summ<=0:
            return 0
        if dp[n][summ]!=-1:
            return dp[n][summ]
        if arr[n-1]<=summ:
            dp[n][summ]=min(1+self.unboundknapsack(arr,n,summ-arr[n-1],dp),self.unboundknapsack(arr,n-1,summ,dp))
        else:
            dp[n][summ]=self.unboundknapsack(arr,n-1,summ,dp)
        return dp[n][summ]
    def numSquares(self, n: int) -> int:
        arr=[]
        i=1
        while i*i<=n:
            arr.append(i*i)
            i+=1
        dp=[[-1 for i in range(n+1)]for j in range(len(arr)+1)]    
        ans=self.unboundknapsack(arr,len(arr),n,dp) 
        if ans==float('inf'):
            return 1
        return ans
   
        