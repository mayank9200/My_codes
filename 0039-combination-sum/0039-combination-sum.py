class Solution:
    def rec(self,pos,candidates,target,ans,res):
        if target<0:
            return
        if target==0:
            res.append(ans)
            return
        if pos==len(candidates):
            return 
        self.rec(pos,candidates,target-candidates[pos],ans+[candidates[pos]],res)
        while pos+1<len(candidates) and candidates[pos]==candidates[pos+1]:
            pos+=1
        self.rec(pos+1,candidates,target,ans,res)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        res=[]
        candidates.sort()
        self.rec(0,candidates,target,ans,res)
        return res
        