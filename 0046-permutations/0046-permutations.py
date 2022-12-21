class Solution:
    def rec(self,pos,nums,ans,res,n):
        if pos==n-1:
            res.append(nums[:])
            return 
        for i in range(pos,n):  
            nums[i],nums[pos]=nums[pos],nums[i]
            self.rec(pos+1,nums,ans,res,n)
            nums[i],nums[pos]=nums[pos],nums[i]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]
        n=len(nums)
        pos=0
        self.rec(pos,nums,ans,res,n)
        return res
        # tc= o(n!*n*n)
        