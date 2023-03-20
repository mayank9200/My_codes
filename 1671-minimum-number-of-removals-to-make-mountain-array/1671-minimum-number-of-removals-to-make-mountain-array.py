class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        #https://www.youtube.com/watch?v=jdfpGSSyN2I&list=PL-Jc9J83PIiEZvXCn-c5UIBvfT8dA-8EG&index=11
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
        #find lds(longest decreasing subsequence)    
        for i in range(n-2,-1,-1):
            maxx=0
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    maxx=max(maxx,lds[j])
            lds[i]=maxx+1
        max_bitnoic=0
        for i in range(n):
            if lis[i]>1 and lds[i]>1: #if any one of them has value 1 means it is strictly increasing/decreasing but we have to find mountain hence both should be greater than 1
                max_bitnoic=max(max_bitnoic,lis[i]+lds[i]-1) #find max bitnoic array length
        return n-max_bitnoic #minimum removals are total elements-elements involved in max bitnoic array
            
        
        