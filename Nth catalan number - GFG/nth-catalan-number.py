#User function Template for python3

class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        if n==0 or n==1:
            return 1
        dp=[0 for i in range(n+1)]
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]=dp[i]+dp[j]*dp[i-j-1]
        return dp[n]        
        #return the nth Catalan number.


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        
        print(Solution().findCatalan(n))
        
# } Driver Code Ends