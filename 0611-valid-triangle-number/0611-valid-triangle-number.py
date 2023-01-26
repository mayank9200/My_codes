class Solution:
    def solve(self,arr,start,end,k):
        c=0
        #print(start,end)
        while start<end:
            if arr[start]+arr[end]>k:
                c=c+(end-start)
                end-=1
            else:
                start+=1
        return c
            
            
    
    
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        count=0
        for i in range(n-1,1,-1):
            k=nums[i]
            count+=self.solve(nums,0,i-1,k)
        return count    
            
        