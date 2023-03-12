class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin,currmax=1,1
        ans=max(nums)
        n=len(nums)
        for i in range(n):
            currmaxx=currmax
            currmax=max(nums[i]*currmax,nums[i]*currmin,nums[i])
            currmin=min(nums[i]*currmaxx,nums[i]*currmin,nums[i])
            
            #print(currmin,currmax)
            ans=max(ans,max(currmin,currmax))
        return ans    
           
            
            
        