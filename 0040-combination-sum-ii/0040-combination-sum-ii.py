class Solution:
    import sys
    sys.setrecursionlimit(10**6)
    def rec(self,pos,candidates,target,ans,res,s):
        if target<0:
            return
        if target==0:
            res.append(ans)
            return
        if pos==len(candidates):
            return 
        self.rec(pos+1,candidates,target-candidates[pos],ans+[candidates[pos]],res,s)
        while pos+1<len(candidates) and candidates[pos]==candidates[pos+1]:
            pos+=1
        self.rec(pos+1,candidates,target,ans,res,s)
            
            
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        res=[]
        candidates.sort()
        s=set()
        self.rec(0,candidates,target,ans,res,s)
        return res