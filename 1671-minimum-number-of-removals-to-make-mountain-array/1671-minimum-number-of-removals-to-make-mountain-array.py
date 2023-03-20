class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[0 for i in range(n)]
        lds=[0 for i in range(n)]
        lis[0]=1
        lds[n-1]=1
        #find lis for each position
        for i in range(1,n):
            maxx=0
            for j in range(i):
                if nums[j]<nums[i]:
                    maxx=max(maxx,lis[j])
            lis[i]=maxx+1
        for i in range(n-2,-1,-1):
            maxx=0
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    maxx=max(maxx,lds[j])
            lds[i]=maxx+1
        max_bitnoic=0
        for i in range(n):
            if lis[i]>1 and lds[i]>1:
                max_bitnoic=max(max_bitnoic,lis[i]+lds[i]-1)
        return n-max_bitnoic    
            
        
        