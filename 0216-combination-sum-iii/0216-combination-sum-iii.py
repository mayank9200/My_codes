class Solution:
    def rec(self,val,target,k,ans,res):
        if target<0:
            return
        if target==0 and len(ans)==k:
            res.append(ans[:])
            return 
        if val>9:
            return 
        if len(ans)>k:
            return
        ans.append(val)
        self.rec(val+1,target-val,k,ans,res)
        ans.pop()
        self.rec(val+1,target,k,ans,res)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        val=1
        ans=[]
        res=[]
        self.rec(val,n,k,ans,res)
        return res