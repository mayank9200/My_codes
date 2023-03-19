class Solution:
    def solve(self,ip,op,ind,n,k,ans,v):
        if ind==n:
            ans[0]+=1
            return  
        if v[ip[ind]-k]==0:
            v[ip[ind]]+=1
            self.solve(ip,op+[ip[ind]],ind+1,n,k,ans,v)
            v[ip[ind]]-=1
        self.solve(ip,op,ind+1,n,k,ans,v)
        return
        
        
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=[0]
        nums.sort()
        op=[]
        s=set()
        v=[0 for i in range(1001)]
        self.solve(nums,[],0,n,k,ans,v)
        return ans[0]-1
        