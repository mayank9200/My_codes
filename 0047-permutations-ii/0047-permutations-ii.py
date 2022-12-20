class Solution:
    def rec(self,nums,ans,res,n,s):
        if len(ans)==n:
            if tuple(ans) not in s: 
                res.append(ans)
                s.add(tuple(ans))
            return
        for i in range(len(nums)):
            temp=nums[i]
            nums.pop(i)
            self.rec(nums,ans+[temp],res,n,s)
            nums.insert(i,temp)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]
        s=set()
        self.rec(nums,ans,res,len(nums),s)
        return res
        
        