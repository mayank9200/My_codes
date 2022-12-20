class Solution:
    def rec(self,nums,ans,res,n):
        if len(ans)==n:
            res.append(ans)
            return
        for i in range(len(nums)):
            temp=nums[i]
            nums.pop(i)
            self.rec(nums,ans+[temp],res,n)
            nums.insert(i,temp)
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]
        self.rec(nums,ans,res,len(nums))
        return res
        
        