class Solution:
    def rec(self,index,arr,target,ans,res):
        if target<0:
            return 
        if index==len(arr):
            if target==0:
                res.append(ans)
                return     
            return        
        self.rec(index,arr,target-arr[index],ans+[arr[index]],res)
        self.rec(index+1,arr,target,ans,res)
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        res=[]
        self.rec(0,candidates,target,ans,res)
        return res
        