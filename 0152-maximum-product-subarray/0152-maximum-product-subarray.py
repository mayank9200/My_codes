class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #https://www.youtube.com/watch?v=lXVy6YWFcRM
        currmin,currmax=1,1
        ans=max(nums)
        n=len(nums)
        for i in range(n):
            currmaxx=currmax #creating a temp because in next line its value changes
            currmax=max(nums[i]*currmax,nums[i]*currmin,nums[i]) #calculation with previous max subarray product
            currmin=min(nums[i]*currmaxx,nums[i]*currmin,nums[i]) #calculation with previous min subarray product
            ans=max(ans,max(currmin,currmax)) #max till now after multiplying both with min and max subarray
        return ans    #final ans
           
            
            
        