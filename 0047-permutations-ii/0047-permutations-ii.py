class Solution:
    def rec(self,pos,nums,ans,res,n):
        if pos==n-1:
            res.append(nums[:])
            return 
        s=set()
        for i in range(pos,n):
            if nums[i] in s:
                continue
            s.add(nums[i])    
            nums[i],nums[pos]=nums[pos],nums[i]
            self.rec(pos+1,nums,ans,res,n)
            nums[i],nums[pos]=nums[pos],nums[i]
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]
        n=len(nums)
        pos=0
        self.rec(pos,nums,ans,res,n)
        return res
        