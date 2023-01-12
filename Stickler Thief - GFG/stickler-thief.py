#User function Template for python3

class Solution:  
    def rec(self,arr,n,dp):
        if n<0:
            return 0
        if n==0:
            return arr[0]
        if dp[n]!=-1:
            return dp[n]
        t1=(arr[n]+self.rec(arr,n-2,dp))
        t2=self.rec(arr,n-1,dp)
        dp[n]=max(t1,t2)
        return dp[n]
            
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        dp=[-1]*len(a)
        ans=self.rec(a,n-1,dp)
        return ans
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends