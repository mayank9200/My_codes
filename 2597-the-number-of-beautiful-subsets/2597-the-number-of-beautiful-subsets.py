class Solution:
    def solve(self,ip,op,ind,n,k,ans,v):
        if ind==n:
            ans[0]+=1
            return  
        if v[ip[ind]-k]==0: #if element-k not in taken till now
            v[ip[ind]]+=1 #will take that element
            self.solve(ip,op+[ip[ind]],ind+1,n,k,ans,v) #case for taking
            v[ip[ind]]-=1 #will remove that element
        self.solve(ip,op,ind+1,n,k,ans,v) #case for not taking
        return
        
        
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort() #sort just to see nums[i]-k in array
        ans=[0]
        op=[]
        v=[0 for i in range(1001)] 
        self.solve(nums,[],0,n,k,ans,v)
        return ans[0]-1
        