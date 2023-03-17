class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
    #     #meaning of dp is starting at the particular position what is the max to reach till last index
    #     n=len(nums)
    #     dp=[0 for i in range(n)]
    #     dp[n-1]=nums[n-1] #from last to last is the value itself
    #     for i in range(n-2,-1,-1):
    #         maxx=float('-inf')
    #         for j in range(i+1,i+1+k): # check max value of all k above it
    #             if j<n:
    #                 maxx=max(maxx,dp[j]) 
    #         dp[i]=nums[i]+maxx   #simply add the max value along with starting pos value
    #     return dp[0] #it gives max value starting from pos 0
    # #TC-O(n*k)
        from heapq import heappush,heappop
        n=len(nums)
        h=[]
        dp=[0 for i in range(n)]
        dp[n-1]=nums[n-1] #from last to last is the value itself
        heappush(h,[-dp[n-1],n-1])
        for i in range(n-2,-1,-1):
            while len(h)>0 and h[0][1]>i+k:
                heappop(h)
            dp[i]=nums[i]+(0 if len(h)==0 else -h[0][0])
            heappush(h,[-dp[i],i])
        #print(dp)       
        return dp[0] #it gives max value starting from pos 0
    #TC-O(n*k)
        